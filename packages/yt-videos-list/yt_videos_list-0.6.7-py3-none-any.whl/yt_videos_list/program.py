import re
import os
import time
import datetime
import threading
import selenium
from . import scroller, writer
from .notifications import Common
from .custom_logger import log, log_time_taken
def determine_action(url, driver, video_id_only, scroll_pause_time, verify_page_bottom_n_times, reverse_chronological, file_name, file_buffering, txt, csv, markdown, all_video_data_in_memory, logging_locations):
 common_message = Common()
 txt_exists = os.path.isfile(f'{file_name}.txt') if txt else False
 csv_exists = os.path.isfile(f'{file_name}.csv') if csv else False
 md_exists = os.path.isfile(f'{file_name}.md') if markdown else False
 force_to_page_bottom = False
 txt_videos = set()
 csv_videos = set()
 md_videos = set()
 common_visited_videos = set()
 current_condition = (txt, txt_exists, csv, csv_exists, markdown, md_exists)
 update_conditions = set(
  (
   (True, True, True, True, True, True),
   (True, True, True, True, False, False),
   (True, True, False, False, True, True),
   (False, False, True, True, True, True),
   (True, True, False, False, False, False),
   (False, False, False, False, True, True),
   (False, False, True, True, False, False),
  )
 )
 if not all_video_data_in_memory and current_condition in update_conditions: log(f'Detected an existing file with the name {file_name} in this directory, checking for new videos to update {file_name}....', logging_locations)
 else: force_to_page_bottom = True
 videos_list, txt_videos, csv_videos, md_videos, common_visited_videos = scroller.scroll_until_break(url, driver, scroll_pause_time, logging_locations, verify_page_bottom_n_times, force_to_page_bottom, file_name, txt_exists, csv_exists, md_exists)
 if len(videos_list) == 0:
  log(common_message.no_videos_found, logging_locations)
  return None
 video_data = load_video_data(videos_list, common_visited_videos, video_id_only, reverse_chronological, logging_locations)
 use_threads = (int(txt) + int(csv) + int(markdown)) > 1
 csv_writer = None
 identifier = 'Video ID' if video_id_only is True else 'Video URL'
 if use_threads:
  #
  threads = []
  def call(function, file_type, file_visited_videos):
   newline = '' if file_type == 'csv' else None
   if function == 'update_file': return threading.Thread(target=writer.update_file, args=(file_type, file_name, file_buffering, newline, csv_writer, now(), logging_locations, identifier, reverse_chronological, video_data, file_visited_videos, video_id_only))
   else: return threading.Thread(target=writer.create_file, args=(file_type, file_name, file_buffering, newline, csv_writer, now(), logging_locations, identifier, reverse_chronological, video_data))
  if txt:
   if txt_exists: txt_thread = call('update_file', 'txt', txt_videos)
   else: txt_thread = call('create_file', 'txt', set())
   txt_thread.start()
   threads.append(txt_thread)
  if csv:
   if csv_exists: csv_thread = call('update_file', 'csv', csv_videos)
   else: csv_thread = call('create_file', 'csv', set())
   csv_thread.start()
   threads.append(csv_thread)
  if markdown:
   if md_exists: md_thread = call('update_file', 'md', md_videos)
   else: md_thread = call('create_file', 'md', set())
   md_thread.start()
   threads.append(md_thread)
  for thread in threads:
   thread.join()
 else:
  def call(function, file_type, file_visited_videos):
   newline = '' if file_type == 'csv' else None
   if function == 'update_file': return writer.update_file(file_type, file_name, file_buffering, newline, csv_writer, now(), logging_locations, identifier, reverse_chronological, video_data, file_visited_videos, video_id_only)
   else: return writer.create_file(file_type, file_name, file_buffering, newline, csv_writer, now(), logging_locations, identifier, reverse_chronological, video_data)
  if txt:
   if txt_exists: call('update_file', 'txt', txt_videos)
   else: call('create_file', 'txt', set())
  if csv:
   if csv_exists: call('update_file', 'csv', csv_videos)
   else: call('create_file', 'csv', set())
  if markdown:
   if md_exists: call('update_file', 'md', md_videos)
   else: call('create_file', 'md', set())
 return video_data
def now():
 return datetime.datetime.now().isoformat().replace(':', '_').replace('.', '-')
def load_video_data(videos_list, common_visited_videos, video_id_only, reverse_chronological, logging_locations):
 video_loading_cpu_start_time = time.perf_counter()
 video_loading_real_start_time = time.time()
 log('Loading video information into memory...', logging_locations)
 video_data = []
 video_number = len(videos_list)
 videos_to_load = video_number
 for videos_loaded, selenium_element in enumerate(videos_list, start=1):
  video_title = selenium_element.get_attribute('title')
  video_title = normalize_whitespace(video_title)
  video_url = selenium_element.get_attribute('href').replace('shorts/', 'watch?v=').split('&pp')[0]
  try:
   video_duration = selenium_element.find_element_by_xpath('./../../../../div[@id="thumbnail"]/ytd-thumbnail/a[@id="thumbnail"]/div[@id="overlays"]/ytd-thumbnail-overlay-time-status-renderer/div/span[@class="style-scope ytd-thumbnail-overlay-time-status-renderer"]').get_attribute('innerHTML').split()[0]
  except selenium.common.exceptions.NoSuchElementException:
   video_duration = 'N/A'
   log(f'Video {videos_loaded + 1} did not have a "Video Duration" field, storing as "N/A"...', logging_locations)
  if common_visited_videos and video_url in common_visited_videos:
   continue
  video_data.append([video_number, video_title, video_duration, video_url])
  video_number -= 1
  if videos_loaded % 250 == 0:
   log(f'Loaded {videos_loaded} videos into memory...', logging_locations)
 if reverse_chronological is False:
  video_data.reverse()
 log_time_taken(video_loading_cpu_start_time, video_loading_real_start_time, 'It took ', f' to load information for {videos_to_load} videos into memory\n', logging_locations)
 if video_id_only is True:
  log('Keeping only the video ID from the full video URL...', logging_locations)
  for video_datum in video_data:
   full_url = video_datum[3]
   video_id = full_url.split('watch?v=')[1]
   video_datum[3] = video_id
  log('Finished formatting the video IDs...\n', logging_locations)
 return video_data
def normalize_whitespace(raw_text):
 text_with_newline_and_cr_removed = re.sub('[\n\r]+', ' ', raw_text)
 normalized_text = re.sub('\s{2,}', ' ', text_with_newline_and_cr_removed).strip()
 return normalized_text

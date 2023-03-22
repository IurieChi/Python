#Look on directory check metata data and rename photo with created day

from datetime import datetime
from pathlib import Path

def generate_created_date(path):
    stat_result = path.stat()
    creation_day = stat_result.st_birthtime
    # Windows --> stat_result.st_ctime
	# Other Unix --> stat_result.st_ctime (last modification date)
	# Other Linux --> stat_result.st_mtime (last modification date)
    utc_timestamp = datetime.utcfromtimestamp(creation_day)
    return utc_timestamp.strftime('%m_%y_')

def rename_image(image_folder):
    type_file = ['.png','.svg']
    for path in Path(image_folder).iterdir():
        if path.is_file()and path.suffix in type_file:
            print(f"Rename {path.stem}" )
            date = generate_created_date(path)
            new_path = Path(image_folder + date + path.stem + path.suffix)
            path.rename(new_path)


#call function 

rename_image('files/images/')


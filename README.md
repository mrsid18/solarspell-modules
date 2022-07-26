# Solarspell Modules

There are 2 parts in this repo. 

1. Generating database script - `generate_db.py`
2. API - to be hosted on the server.

## Generating Database

1. Go to desired modules folder
      
        cd /path/to/modules/folder 

2. Inside the modules folder, copy the `generate_db.py` here and Run
        
        python3 generate_db.py 
        
## API

1. Copy the generated `module.db` to the db folder.
2. Set `root_path` in `files.php` and `category.php`

        $root_path = "/path/to/modules/folder/on/server"; //path without trailing slash '/'



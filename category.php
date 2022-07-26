<?php
// Gets files by category/subcategory id
header("Access-Control-Allow-Origin: *");

$db = new SQLite3('./db/module.db');

$category_id = (int)$_GET['id'];

$root_path = ""; // path to the root directory of the files

$query = $db->query('SELECT * FROM files JOIN categories ON files.category_id = categories.id WHERE category_id='.$category_id.' ORDER BY files.name');

$files = array();

while ($row = $query->fetchArray()) {
    $file_path = $root_path.$row["path"].'/'.$row[1];
    $files[] = [
        'id' => $row[0],
        'name' => $row[1],
        'size' => $row["size"],
        'file_path'=> $file_path,
        'category_id' => $row["category_id"],
        'category_name' => $row[5],
    ];
}

print(json_encode($files, JSON_UNESCAPED_SLASHES));




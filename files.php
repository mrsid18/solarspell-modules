<?php

header("Access-Control-Allow-Origin: *");

$db = new SQLite3('./db/module.db');

$query = $db->query('SELECT * FROM files join categories on files.category_id = categories.id');

$files = array();

while ($row = $query->fetchArray()) {
    $files[] = [
        'id' => $row[0],
        'name' => $row[1],
        'size' => $row["size"],
        'file_path'=> $row[5].'/'.$row[1],
        'category_id' => $row["category_id"],
        'category_name' => $row[5],
    ];
}

print(json_encode($files, JSON_UNESCAPED_SLASHES));




<?php

header("Access-Control-Allow-Origin: *");

$db = new SQLite3('./db/module.db');

$query = $db->query('SELECT * FROM categories');

$categories = array();

while ($row = $query->fetchArray()) {
    $categories[] = [
        'id' => $row['id'],
        'name' => $row['name'],
    ];
}
 
print(json_encode($categories));




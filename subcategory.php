<?php
// Gets all subcategories by category id
header("Access-Control-Allow-Origin: *");

$db = new SQLite3('./db/module.db');

$parent_id = (int)$_GET['parent_id'];

$query = $db->query('SELECT * FROM categories WHERE parent_id='.$parent_id.' ORDER BY name');

$subcategories = array();

while ($row = $query->fetchArray()) {
    $subcategories[] = [
        'id' => $row['id'],
        'name' => $row['name'],
    ];
}
 
print(json_encode($subcategories));




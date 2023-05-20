<?php
// Подключение к базе данных
$servername = "localhost";
$username = "postgres";
$password = "1003";
$dbname = "project1";

// Создание подключения
$conn = new mysqli($servername, $username, $password, $dbname);

// Проверка соединения
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Получение данных из POST-запроса
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $headline = $_POST["headline"];
    $content = $_POST["content"];

    // Проверка и обработка данных по необходимости

    // Подготовка и выполнение SQL-запроса для вставки данных
    $sql = "INSERT INTO articles (headline, content) VALUES (?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ss", $headline, $content);

    if ($stmt->execute()) {
        echo "Данные успешно добавлены в базу данных.";
    } else {
        echo "Ошибка при добавлении данных: " . $conn->error;
    }

    $stmt->close();
}

// Закрытие соединения с базой данных
$conn->close();
?>

# COM-Port Camera Shutter

## English Version

### Overview
This Python script allows you to control a camera connected to your computer via a serial COM port. It works with any camera connected to your system, capturing images in response to commands sent through the COM port. The images are saved in a designated subfolder, which can later be used to create a timelapse video in a video editor. The script is simple to set up and run, making it ideal for creating timelapses of 3D printing projects.

### Features
- **Universal Camera Compatibility**: Works with any connected camera.
- **Automated Image Capture**: Takes snapshots on receiving the "SMILE" command from the COM port.
- **Organized File Management**: Saves images in a timestamped subfolder.
- **Simple Workflow**: Start and stop the script with minimal configuration.
- **Timelapse Creation**: Easily stitch the saved images into a video using any video editor.

### Installation and Setup

1. **Clone the Repository**:
   - Download the script from the GitHub repository:
     ```bash
     git clone https://github.com/LemanRus/COM-Port-Camera-Shutter
     ```
   - Or download directly from releases

2. **Prepare the Working Directory**:
   - Place the `main_eng.py` file into the folder where you want to save the captured images.

3. **Configure Your 3D Printer Slicer**:
   - If you are using Ultimaker Cura:
     - Go to **Extensions > Post Processing > Modify G-Code > Add a Script > Time Lapse**.
       - Add the command `M118 SMILE` after each layer to trigger the camera.
     - Add the command `M118 FINISH` at the end of the print to stop the script.

4. **Start Your Print and Run the Script**:
   - Begin the 3D printing process on your printer.
   - Run the Python script from the command line or PowerShell:
     ```bash
     python main_eng.py
     ```
   - The script will start capturing images as soon as it receives the "SMILE" command. It will automatically stop when it receives the "FINISH" command.


## Русская версия

### Обзор
Этот скрипт на Python позволяет управлять камерой, подключенной к вашему компьютеру через последовательный COM-порт. Он работает с любой подключенной камерой, захватывая изображения в ответ на команды, отправленные через COM-порт. Изображения сохраняются в отдельную подпапку, которую затем можно использовать для создания таймлапс-видео в видеоредакторе. Скрипт прост в настройке и использовании, что делает его идеальным для создания таймлапсов 3D-печати.

### Особенности
- **Универсальная совместимость с камерами**: Работает с любой подключенной камерой.
- **Автоматическая съемка**: Делает снимки при получении команды "SMILE" через COM-порт.
- **Упорядоченное управление файлами**: Сохраняет изображения в подпапке с временной меткой.
- **Простой рабочий процесс**: Запуск и остановка скрипта требуют минимальных настроек.
- **Создание таймлапса**: Легко склеивайте сохраненные изображения в видео с помощью любого видеоредактора.

### Установка и настройка

1. **Скачайте репозиторий**:
   - Загрузите скрипт из GitHub репозитория:
     ```bash
     git clone https://github.com/LemanRus/COM-Port-Camera-Shutter
     ```
   - Или напрямую из раздела "releases"

2. **Подготовьте рабочий каталог**:
   - Поместите файл `main_rus.py` в папку, где вы хотите сохранять снимки.

3. **Настройте слайсер вашего 3D-принтера**:
   - Если вы используете Ultimaker Cura:
     - Перейдите в **Расширения > Постобработка > Изменить G-код > Добавить скрипт > Time Lapse**.
       - Добавьте команду `M118 SMILE` после каждого слоя для активации камеры.
     - Добавьте команду `M118 FINISH` в конце печати для остановки скрипта.

4. **Запустите печать и скрипт**:
   - Начните процесс 3D-печати на вашем принтере.
   - Запустите Python скрипт из командной строки или PowerShell:
     ```bash
     python main_rus.py
     ```
   - Скрипт начнет захват изображений сразу после получения команды "SMILE". Он автоматически остановится после получения команды "FINISH".

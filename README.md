# Map with Markers

This project is a simple web application that allows users to add and view markers on a map. Markers include details like a name, description, informant information, media link, and optional media files.

## Requirements

- Python 3.x
- Flask
- JSON
- Leaflet.js
- Folium

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/map-with-markers.git
    cd map-with-markers
    ```

2. Install the required dependencies:

    ```bash
    pip install Flask folium
    ```

3. Create the necessary folders:

    ```bash
    mkdir uploads
    mkdir templates
    ```

4. Add the `index.html` and `map.html` files to the `templates` folder.

## Running the Application

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to:

    ```
    http://127.0.0.1:5000/
    ```

## Features

- **Add Markers:** Users can add markers to the map with details like name, description, informant, media link, and media files.
- **View Markers:** Existing markers are displayed on the map. Clicking a marker will display its details.
- **File Upload:** Users can upload media files (images, videos, etc.) when adding markers. These files are stored in the `uploads` folder.

## File Structure

- `app.py`: The main application script.
- `markers.txt`: Stores the markers in JSON format.
- `uploads/`: Stores uploaded media files.
- `templates/`: Stores HTML files (`index.html`, `map.html`).

## Notes

- Ensure that the `index.html` and `map.html` files are placed in the `templates` folder.
- The `uploads` folder will be created automatically if it does not exist.
- All markers are stored in the `markers.txt` file in JSON format.

## Dependencies

- Flask
- Leaflet.js

## License

This project is licensed under the MIT License. See the [MIT License](LICENSE) file for details.


## Feel free to modify the content to fit your specific project details!


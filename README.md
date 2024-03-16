# URL Info Web App

## Overview

URL Info Web App is a web application that takes a URL as input and provides detailed information about the URL, including IP address, ISP, ASN, organization, and more. It utilizes a combination of Python Flask for the backend, React for the frontend, WebSocket for real-time updates, and several other technologies.

## Features

- **URL Information Retrieval**: Input a URL and get detailed information about it.
- **Real-time Updates**: Utilizes WebSocket for real-time updates and notifications.
- **Responsive Design**: Built with React, ensuring a responsive and user-friendly interface.
- **Backend API**: Provides a robust backend API powered by Python Flask for handling URL information retrieval.
- **Technological Stack**: Leveraging the power of Flask, React, WebSocket, and various other technologies for a seamless user experience.
## Demo Shorts
- ** Enter URL
- ![17 03 2024_00 45 14_REC](https://github.com/Vicky8180/URL-Insight/assets/76256436/ebda3737-9d83-41a5-a784-2a96cb4dc4f0)

  - ** Get Deatils
  - ![17 03 2024_00 45 44_REC](https://github.com/Vicky8180/URL-Insight/assets/76256436/28fb7862-4494-429c-9e33-7a9982476acb)
 
  - ![17 03 2024_00 46 20_REC](https://github.com/Vicky8180/URL-Insight/assets/76256436/3324e028-7205-410c-945b-293f352f579d)


## Technologies Used

### Backend
- Python Flask
- WebSocket (for real-time updates)
- Flask-SocketIO
- Requests (for fetching URL information)
- BeautifulSoup (for web scraping, if applicable)

### Frontend
- React
- Axios (for making HTTP requests)
- Bootstrap (for styling and layout)

## Installation

### Prerequisites

- Python 3.x
- Node.js
- npm (Node Package Manager)

### Backend Setup

1. Clone the repository:

    ```
    git clone https://github.com/Vicky8180/URL-Insight
    ```

2. Navigate to the backend directory:

    ```
    cd URL-Insight/backend
    ```

3. Install Python dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Run the Flask server:

    ```
    flask run
    ```

### Frontend Setup

1. Navigate to the frontend directory:

    ```
    cd URL-Insight/frontend
    ```

2. Install npm dependencies:

    ```
    npm install
    ```

3. Run the React development server:

    ```
    npm start
    ```

4. Open your browser and navigate to `http://localhost:3000` to view the application.

## Usage

1. Enter a URL into the input field.
2. Click the "Get Info" button.
3. Wait for the application to fetch and display the URL information.
4. Real-time updates, if implemented, will be displayed automatically.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

# Web Crawler 
## Table of Contents
1. [Introduction](#introduction)
2. [Code Overview](#code-overview)
   1. [Imports](#imports)
   2. [User Interface](#user-interface)
   3. [Crawl Function](#crawl-function)
   4. [Main Execution](#main-execution)
3. [Functionality](#functionality)
   1. [User Input](#user-input)
   2. [Crawling Process](#crawling-process)
   3. [Error Handling](#error-handling)
4. [Potential Improvements](#potential-improvements)
5. [Conclusion](#conclusion)

## Introduction

This report provides a detailed analysis of the "Web Crawler" project, which is implemented in a Python file named `main.py`. The web crawler is a program that systematically browses and collects information from websites, starting from a given root URL and following links to a specified depth.
![alt text](https://github.com/AryanDahiya00/Web-Crawler/blob/main/Capture.JPG)
## Code Overview

The code is structured into several key components:

### Imports

The script starts by importing the necessary libraries and modules:

- `streamlit`: A Python library for building interactive web applications.
- `requests`: A library for making HTTP requests.
- `BeautifulSoup`: A library for parsing HTML and XML documents.
- `urljoin`: A function from the `urllib.parse` module to construct absolute URLs from relative ones.
- `validators`: A library for validating various types of data, including URLs.

### User Interface

The code sets up a Streamlit-based user interface, which includes:

- A title for the application: "Web Crawler"
- A sidebar header: "Crawler Settings"
- A text input field for the user to enter the root URL
- A number input field for the user to set the crawling depth
- A button to start the crawling process

### Crawl Function

The core of the application is the `crawl_url` function, which takes the root URL and the maximum depth as input. This function recursively crawls the website, starting from the root URL and following links to the specified depth. It keeps track of the visited URLs and the status of each crawled link (URL, depth level, and status code/error message).

### Main Execution

The final part of the code handles the main execution flow. When the user clicks the "Start Crawling" button, the script checks if the provided root URL is valid. If so, it calls the `crawl_url` function and displays the crawled links in a table within the Streamlit application.

## Functionality

The web crawler application provides the following key functionality:

### User Input

The user can specify the root URL and the maximum crawling depth through the Streamlit interface. This allows the user to customize the crawling parameters based on their needs.

### Crawling Process

The `crawl_url` function recursively visits the links found on each page, up to the specified depth. It keeps track of the visited URLs to avoid duplicates and collects information about each link, including the URL, depth level, and status code or error message.

### Error Handling

The crawling process includes error handling to gracefully handle any exceptions that may occur during the HTTP requests, such as timeout errors or connection issues. When an error is encountered, the link information is still recorded with the appropriate error message.

## Potential Improvements

While the current implementation provides a functional web crawler, there are a few areas where the code could be further improved:

1. **Concurrency**: The crawling process could be made more efficient by introducing concurrent processing, allowing multiple links to be crawled simultaneously.
2. **Filtering and Customization**: The user interface could be expanded to allow more customization, such as filtering crawled links by status code or depth level, or excluding certain domains or URL patterns.
3. **Data Persistence**: The crawled data could be saved to a file or database for later analysis and reuse, instead of only displaying the results within the Streamlit application.
4. **Robots.txt Handling**: The crawler could be enhanced to respect the robots.txt file of each website, which specifies which pages should not be crawled.
5. **Depth-first vs. Breadth-first Crawling**: The current implementation uses a depth-first approach, but a breadth-first approach could also be implemented as an alternative crawling strategy.

## Conclusion

The "Web Crawler" project provides a basic but functional web crawling application built using Python and the Streamlit library. The code is well-structured and easy to understand, with clear separation of concerns between the user interface, crawling logic, and error handling. While there are opportunities for further improvement, the current implementation serves as a solid foundation for a web crawling tool.


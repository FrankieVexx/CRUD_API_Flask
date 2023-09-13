# Flask Company API

This is a simple Flask application that provides API endpoints to create, read, update, and delete company records. It uses a JSON file ('company.json') to store the company data.

## Installation

1. Clone this repository:

2. Install the required dependencies:

3. Run the Flask application:


## Usage

### Create a New Company

Endpoint: `/create` (HTTP POST)

To create a new company, send a JSON POST request to the `/create` endpoint with the company data in the request body.

Example JSON request:
```json
{
 "id": 1,
 "name": "Example Company",
 "location": "Example location",
 "CEO": "Example CEO",
 "Year-founded": "Example year"
}
```

### Read All Records

Endpoint: /read (HTTP GET)

To retrieve a list of all company records, send an HTTP GET request to the /read endpoint.

Read a Specific Record by ID

Endpoint: /read/<int:record_id> (HTTP GET)

To retrieve a specific company record by its ID, send an HTTP GET request to the /read/<record_id> endpoint.

Example request: /read/1

### Update a Company by ID

Endpoint: /update/<int:record_id> (HTTP PUT)

To update an existing company record by its ID, send a JSON PUT request to the /update/<record_id> endpoint with the updated company data.

Example JSON request:
```json
{
 "id": 1,
 "name": "Example Company",
 "location": "Example location",
 "CEO": "Example CEO",
 "Year-founded": "Example year"
}
```
### Delete a Company by ID

Endpoint: /delete/<int:record_id> (HTTP DELETE)

To delete a company record by its ID, send an HTTP DELETE request to the /delete/<record_id> endpoint.

Example request: /delete/1

JSON Data Format
The JSON data for company records should have the following format:
```json
{
 "id": 1,
 "name": "Example Company",
 "location": "Example location",
 "CEO": "Example CEO",
 "Year-founded": "Example year"
}
```
Example Usage
You can use tools like curl or API clients like Postman to interact with the API endpoints.




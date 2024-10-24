
#!/bin/bash

url="https://lab03-2-brianmethodicalcompany-240830225929.us-central1.run.app/api/chat"


# Define the input message in JSON format
json_data=$(cat <<EOF
{
  "message": "what color does blue and red make?"
}
EOF
)

# Use cURL to send a POST request with the JSON data
curl -X POST "$url" \
     -H "Content-Type: application/json" \
     -d "$json_data"

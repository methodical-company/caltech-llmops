
#!/bin/bash

url="http://127.0.0.1:5000/api/chat"


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

import requests
import streamlit as st
# Function to fetch and print ORCID educational qualifications and number of works, and verify "expert" status
def get_orcid_education_and_works(orcid_id):
    url = f"https://pub.orcid.org/v3.0/{orcid_id}"
    headers = {"Accept": "application/json"}
    
    # Send a GET request to the ORCID API
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        record = response.json()

        # Extract education qualifications
        education_data = record.get("activities-summary", {}).get("educations", {}).get("education-summary", [])
        has_education = False
        if education_data:
            has_education = True  # Set flag if educational qualifications exist
            print("Educational Qualifications:")
            for edu in education_data:
                institution = edu.get("organization", {}).get("name", "Unknown Institution")
                degree = edu.get("role-title", "Unknown Degree")
                start_date = edu.get("start-date", {}).get("year", {}).get("value", "Unknown Start Date")
                end_date = edu.get("end-date", {}).get("year", {}).get("value", "Ongoing" if not edu.get("end-date") else edu.get("end-date").get("year").get("value"))
                print(f"- {degree} at {institution} ({start_date} - {end_date})")
        else:
            st.markdown("No educational qualifications found.")
        
        # Extract number of works
        works_data = record.get("activities-summary", {}).get("works", {}).get("group", [])
        num_works = len(works_data)
        st.markdown(f"\nNumber of works (e.g., publications, presentations): {num_works}")
        
        # Check if person is an "expert" based on education and number of works
        if has_education and num_works >= 5:
            st.markdown("\nExpert Verified: This person is an expert based on educational qualifications and publications.")
        else:
            st.markdown("\nThis person is not classified as an expert.")
            
    else:
        st.markdown(f"Failed to retrieve record. Status Code: {response.status_code}")

# Replace with a valid ORCID iD
orcid_id = "0009-0005-7728-3779"  # Example ORCID iD
get_orcid_education_and_works(orcid_id)

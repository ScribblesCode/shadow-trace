import streamlit as st   # This library helps us create a web interface for our tool
import requests    # This library lets your code "talk" to the internet

# Header - this gives your tool that "Command Center" feel
st.text("_" * 40)
st.text("    S H A D O W _ T R A C E    v1.0    ")
st.text("      OSINT  RECONNAISSANCE        ")
st.text("_" * 40)

def main():
    # 1. Get the target username from the user
    username = st.text_input("\n[!] ENTER TARGET USERNAME: ")
    print(f"[*] SEARCHING DIGITAL FOOTPRINT FOR: {username}. . .\n")

    # 2. Define the 'intelligence' list (the sites we want to probe)
    # Be careful with the syntax here: 'Name': 'URL'
    if st.button("INITIATE TRACE"):
        st.text(f"[*] SEARCHING DIGITAL FOOTPRINT FOR: {username}. . .\n")
    targets = {
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "WordPress": f"https://{username}.wordpress.com",
        "Twitter": f"https://twitter.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "YouTube": f"https://www.youtube.com/{username}",
    }

    # 3. The 'Engine' (Loop through each site and check if it exists)
    for site_name, url in targets.items():
        try:
            # Send a request to the URL
            response = requests.get(url, timeout=5)

            # Check the status code. 200 = success (User found)
            if response.status_code == 200:
                st.text(f"[+] [FOUND] {site_name}: {url}")
            else:
                st.text(f"[-] [MISS] {site_name}")
                
        except Exception:
            st.text(f"[!] [ERROR] Could not reach {site_name}")

            #4. Save findings to a report file
            # 'w' means 'write' mode - it will create a new file if it doesn't exist
        with open("trace_report.txt", "w") as report:
            report.write(f"SHADOW_TRACE REPORT FOR: {username}\n")
            report.write("_" * 40 + "\n")

            for site, url in targets.items():
                    # We record both the name and the link in our report
                report.write(f"{site}: {url}\n")

        print(f"\n[+] RECON DATA SAVED TO: trace_report.txt")
        print("-" * 40)
        st.text("[*] SCAN COMPLETE. STAY DARK.")


    print("\n[*] SCAN COMPLETE.")
    
    # This tells Python to run the 'main' function when the script starts
if __name__ == "__main__":
    main()
    
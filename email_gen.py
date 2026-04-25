```python
import os
import time
import google.generativeai as genai

# --- Configuration ---
# The API key is provided by the environment at runtime.
apiKey = "" 
genai.configure(api_key=apiKey)

def generate_email_variants(context, developer_info):
    """
    Generates 3 cold email variants using Gemini 2.5 Flash.
    Includes exponential backoff for API reliability.
    """
    model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')
    
    system_prompt = f"""
    You are an expert cold email copywriter. Create 3 distinct email variants based on the job/company description provided.
    
    Variants required:
    1. Short & Punchy (Mobile-friendly, under 100 words)
    2. Professional & Value-First (Focus on ROI and expertise)
    3. Creative & Personality-Driven (Pattern interrupt, unique hook)

    Developer Info for Signature:
    Name: {developer_info['name']}
    Role: Freelance Expert
    
    Rules:
    - Always include a [Subject Line] for each.
    - Use placeholders like [Prospect Name] where appropriate.
    - End each with a professional signature and clear CTA.
    """

    user_query = f"Here is the Job Description/Company Info: {context}"

    # Exponential Backoff Implementation
    for i in range(5):
        try:
            response = model.generate_content(
                contents=[{"parts": [{"text": user_query}]}],
                system_instruction={"parts": [{"text": system_prompt}]}
            )
            return response.text
        except Exception as e:
            wait_time = 2 ** i
            if i == 4:
                return f"Error: All retries failed. {str(e)}"
            time.sleep(wait_time)

def main():
    print("="*50)
    print("      Smart-Cold-Email-AI ✉️ by Hammad Virk")
    print("="*50)
    
    # Simple CLI Interface
    print("\n[Step 1] Paste the Job Description or Company Services below:")
    print("(Press Enter twice or Ctrl+D to finish)")
    
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    context = " ".join(lines)

    if not context.strip():
        print("Error: Context cannot be empty.")
        return

    developer_info = {
        "name": "Hammad Virk"
    }

    print("\n[Step 2] Generating your viral-ready drafts via Gemini AI...")
    result = generate_email_variants(context, developer_info)
    
    print("\n" + "="*50)
    print("RESULTS:")
    print("="*50)
    print(result)
    print("\n" + "="*50)
    print("Pro Tip: Personalize the [Prospect Name] before sending!")

if __name__ == "__main__":
    main()

```
      

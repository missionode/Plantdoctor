from google import genai
from django.conf import settings
import json
import PIL.Image

def analyze_plant_image(image_path):
    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    
    # Use gemini-flash-latest for better compatibility
    model_id = 'gemini-flash-latest'
    
    img = PIL.Image.open(image_path)
    
    # Resize image if too large (speed optimization)
    if img.width > 1024 or img.height > 1024:
        img.thumbnail((1024, 1024))
    
    prompt = """
    Analyze this plant image for diseases or pests. 
    Return the result in strictly valid JSON format with the following keys:
    {
      "disease_name": "Name of the disease",
      "confidence": 0.95,
      "description": "Short description of the issue",
      "immediate_action": "What to do right now (bullet points)",
      "long_term_care": "How to prevent it in the future",
      "recommended_products": [
        {"name": "Specific Product Name (e.g., Ugaoo Neem Oil)", "price": "₹299", "description": "usage", "search_term": "Ugaoo Neem Oil buy online India"}
      ]
    }
    If the plant is healthy, indicate "Healthy" in the disease_name.
    Ensure prices are in INR (₹) and products are available in India.
    """
    
    try:
        response = client.models.generate_content(
            model=model_id,
            contents=[prompt, img]
        )
        
        # Extract JSON from response
        text = response.text
        print(f"AI Raw Response: {text}")
        
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        elif "```" in text:
            text = text.split("```")[1].split("```")[0].strip()
        else:
            # Try to find the first '{' and last '}'
            start = text.find('{')
            end = text.rfind('}')
            if start != -1 and end != -1:
                text = text[start:end+1]
            
        result = json.loads(text)
        print(f"Parsed AI Response: {result}")
        return result
    except Exception as e:
        print(f"Error parsing AI response: {e}")
        return {
            "disease_name": "Unknown Issue",
            "confidence": 0.0,
            "description": f"Could not analyze the image properly. Error: {str(e)}",
            "immediate_action": "Try taking a clearer photo.",
            "long_term_care": "Ensure good lighting.",
            "recommended_products": []
        }

from googletrans import Translator

def translate_text(text, src_lang='en', dest_lang='fr'):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

# Example Usage
text = """செயற்கை நுண்ணறிவு (AI) என்பது மனிதர்களைப் போல சிந்திக்கவும் கற்றுக்கொள்ளவும் திட்டமிடப்பட்ட இயந்திரங்களில் மனித நுண்ணறிவின் உருவகப்படுத்துதலைக் குறிக்கிறது.கற்றல் மற்றும் சிக்கலைத் தீர்ப்பது போன்ற மனித மனதுடன் தொடர்புடைய பண்புகளை வெளிப்படுத்தும் எந்தவொரு இயந்திரத்திற்கும் இந்த சொல் பயன்படுத்தப்படலாம்.
AI தொழில்நுட்பம் இரண்டு முக்கிய வகைகளாக பிரிக்கப்பட்டுள்ளது:
குறுகிய AI (அல்லது பலவீனமான AI): முக அங்கீகாரம், மொழி மொழிபெயர்ப்பு அல்லது சதுரங்கம் விளையாடுவது போன்ற ஒரு குறிப்பிட்ட பணிக்காக வடிவமைக்கப்பட்டு பயிற்சி பெற்றது.
பொது AI (அல்லது வலுவான AI): பகுத்தறிவு, சிக்கலைத் தீர்ப்பது அல்லது கற்றல் போன்ற ஒரு மனிதனால் செய்யக்கூடிய எந்தவொரு அறிவுசார் பணியையும் செய்வதை நோக்கமாகக் கொண்டுள்ளது.
AI ஆராய்ச்சி மற்றும் பயன்பாட்டின் முக்கிய பகுதிகள் பின்வருமாறு:
இயந்திர கற்றல் (எம்.எல்): வெளிப்படையாக திட்டமிடப்படாமல் இயந்திரங்களை தரவிலிருந்து கற்றுக்கொள்ளவும் அவற்றின் செயல்திறனை மேம்படுத்தவும் இயந்திரங்களை இயக்குகிறது.
இயற்கை மொழி செயலாக்கம் (என்.எல்.பி): மனித மொழியைப் புரிந்துகொள்ளவும், விளக்கவும், உருவாக்கவும் இயந்திரங்களை அனுமதிக்கிறது.
ரோபாட்டிக்ஸ்: சுற்றுச்சூழலுடன் தொடர்பு கொள்ள AI ஐ இயற்பியல் அமைப்புகளுடன் ஒருங்கிணைக்கிறது.
கணினி பார்வை: படங்கள் மற்றும் வீடியோக்களிலிருந்து காட்சி தரவை விளக்கவும் புரிந்துகொள்ளவும் இயந்திரங்களை இயக்குகிறது.
நிபுணர் அமைப்புகள்: கட்டமைக்கப்பட்ட வடிவத்தில் குறிப்பிடப்பட்டுள்ள அறிவை மேம்படுத்துவதன் மூலம் மனித முடிவெடுப்பதைப் பிரதிபலிக்கவும்.
நரம்பியல் நெட்வொர்க்குகள்: மனித மூளை கட்டமைப்பால் ஈர்க்கப்பட்டு, இந்த நெட்வொர்க்குகள் செயலாக்குகின்றன மற்றும் தகவல்களை அனுப்புகின்றன.
தொழில்கள் முழுவதும் AI ஏராளமான பயன்பாடுகளைக் கொண்டுள்ளது:
உடல்நலம்: நோயறிதல், தனிப்பயனாக்கப்பட்ட மருத்துவம் மற்றும் மருத்துவ ஆராய்ச்சி.
நிதி: இடர் மதிப்பீடு, மோசடி கண்டறிதல் மற்றும் போர்ட்ஃபோலியோ மேலாண்மை.
போக்குவரத்து: தன்னாட்சி வாகனங்கள் மற்றும் பாதை தேர்வுமுறை.
கல்வி: தனிப்பயனாக்கப்பட்ட கற்றல், புத்திசாலித்தனமான பயிற்சி மற்றும் தானியங்கி தரப்படுத்தல்.
வாடிக்கையாளர் சேவை: சாட்போட்கள், மெய்நிகர் உதவியாளர்கள் மற்றும் உணர்வு பகுப்பாய்வு.
தொழில்களை மாற்றுவதற்கும், நாம் வாழும் மற்றும் வேலை செய்யும் விதத்தில் புரட்சியை ஏற்படுத்துவதற்கும் AIS சாத்தியம் மிகப் பெரியது, மேலும் அதன் தொடர்ச்சியான வளர்ச்சி மற்றும் ஒருங்கிணைப்பு எதிர்காலத்திற்கான அதிக வாக்குறுதியைக் கொண்டுள்ளன."""

translated_text = translate_text(text, src_lang='ta', dest_lang='en')
print(f"Translated Text: {translated_text}")



# Afrikaans - af
# Albanian - sq
# Amharic - am
# Arabic - ar
# Armenian - hy
# Azerbaijani - az
# Basque - eu
# Belarusian - be
# Bengali - bn
# Bosnian - bs
# Bulgarian - bg
# Catalan - ca
# Cebuano - ceb
# Chinese (Simplified) - zh-cn
# Chinese (Traditional) - zh-tw
# Corsican - co
# Croatian - hr
# Czech - cs
# Danish - da
# Dutch - nl
# English - en
# Esperanto - eo
# Estonian - et
# Finnish - fi
# French - fr
# Frisian - fy
# Galician - gl
# Georgian - ka
# German - de
# Greek - el
# Gujarati - gu
# Haitian Creole - ht
# Hausa - ha
# Hawaiian - haw
# Hebrew - he
# Hindi - hi
# Hmong - hmn
# Hungarian - hu
# Icelandic - is
# Igbo - ig
# Indonesian - id
# Irish - ga
# Italian - it
# Japanese - ja
# Javanese - jw
# Kannada - kn
# Kazakh - kk
# Khmer - km
# Korean - ko
# Kurdish (Kurmanji) - ku
# Kyrgyz - ky
# Lao - lo
# Latin - la
# Latvian - lv
# Lithuanian - lt
# Luxembourgish - lb
# Macedonian - mk
# Malagasy - mg
# Malay - ms
# Malayalam - ml
# Maltese - mt
# Maori - mi
# Marathi - mr
# Mongolian - mn
# Nepali - ne
# Norwegian - no
# Pashto - ps
# Persian - fa
# Polish - pl
# Portuguese - pt
# Punjabi - pa
# Romanian - ro
# Russian - ru
# Samoan - sm
# Scots Gaelic - gd
# Serbian - sr
# Sesotho - st
# Shona - sn
# Sindhi - sd
# Sinhala - si
# Slovak - sk
# Slovenian - sl
# Somali - so
# Spanish - es
# Sundanese - su
# Swahili - sw
# Swedish - sv
# Tagalog (Filipino) - tl
# Tajik - tg
# Tamil - ta
# Telugu - te
# Thai - th
# Turkish - tr
# Ukrainian - uk
# Urdu - ur
# Uzbek - uz
# Vietnamese - vi
# Welsh - cy
# Xhosa - xh
# Yiddish - yi
# Yoruba - yo
# Zulu - zu
# You can specify the source (src) and target (dest) languages using their language codes as shown above.









# import tkinter as tk
# from tkinter import scrolledtext, messagebox
# from googletrans import Translator

# def translate_text():
#     try:
#         src_text = input_text_box.get("1.0", tk.END).strip()
#         src_lang = src_lang_entry.get()
#         dest_lang = dest_lang_entry.get()
        
#         if not src_text:
#             messagebox.showwarning("Input Error", "Please enter text to translate.")
#             return
        
#         # Perform the translation
#         translator = Translator()
#         translation = translator.translate(src_text, src=src_lang, dest=dest_lang)
        
#         # Display the translated text
#         output_text_box.delete("1.0", tk.END)
#         output_text_box.insert(tk.END, translation.text)
    
#     except Exception as e:
#         messagebox.showerror("Translation Error", f"An error occurred: {e}")

# # Create the main window
# root = tk.Tk()
# root.title("Text Translator")
# root.geometry("600x400")

# # Source Text Input
# tk.Label(root, text="Enter text to translate:").pack(pady=5)
# input_text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=8)
# input_text_box.pack(pady=5)

# # Source and Destination Language Input
# tk.Label(root, text="Source Language (e.g., 'en'):").pack(pady=5)
# src_lang_entry = tk.Entry(root)
# src_lang_entry.pack(pady=5)

# tk.Label(root, text="Destination Language (e.g., 'es'):").pack(pady=5)
# dest_lang_entry = tk.Entry(root)
# dest_lang_entry.pack(pady=5)

# # Translation Button
# translate_button = tk.Button(root, text="Translate", command=translate_text)
# translate_button.pack(pady=10)

# # Output Text Box
# tk.Label(root, text="Translated text:").pack(pady=5)
# output_text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=8)
# output_text_box.pack(pady=5)

# # Start the Tkinter event loop
# root.mainloop()

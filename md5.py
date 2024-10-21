import hashlib 
def md5_hash(text): 
 return hashlib.md5(text.encode()).hexdigest() 

if __name__ == "__main__": 
 input_text = "supriya" 
 hash_result = md5_hash(input_text) 
 print(f"MD5 hash of '{input_text}': {hash_result}") 

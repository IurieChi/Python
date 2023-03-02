
# ASCII Art Encoding
# Function "encodeString" that will encode a string like 'AAAAABBBBAAA' as a list of tuples: [('A', 5), ('B', 4), ('A', 3)] meaning that the string has "5 A's, followed by 4 B's, followed by 3 A's"
# Then use that function to compress a string containing "ASCII Art" (https://en.wikipedia.org/wiki/ASCII_art)
# Function "decodeString" that will take in a list of tuples and print the original string.

def encodeString(stringVal):
    encodeList =[]
    prevChar = stringVal[0]
    count = 0
    for char in stringVal:
        if prevChar != char:
            encodeList.append((prevChar, count))
            count = 0
        prevChar = char
        count +=1
    encodeList.append((prevChar , count))
    return encodeList
    # print(encodeList)

def decodeString(encodedList):
    decodeStr = ''
    for item in encodedList:
        decodeStr = decodeStr + item[0] * item[1]
    return decodeStr
    

# # Test encodeString function
# print(encodeString('AAAAABBBBCCC'))
# # Test decodeString function
# print(decodeString([('A', 5), ('B', 4), ('C', 3)]))

# will take this image and convert it in to dictionar
# after this decode it back in image 
art = '''                                                                            
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                    %%%%%%%%                         %%%%%%%%                   
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%             
           %%%%%%                                               %%%%%           
          %%%%%                                                   %%%%%         
        %%%%%                                                       %%%%%       
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%     
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%   
    %%%%                    %%%%%              %%%%%                     %%%%   
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%   
    %%%%       %%%%%%                                        %%%%%       %%%%   
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%     
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%         
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                   %%%%%%%%%%%%                                                                                                
'''
#encoding 
encode= encodeString(art)
# decodign 
print(decodeString(encode))


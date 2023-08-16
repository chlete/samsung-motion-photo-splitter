# README                                                                       
                                                                               
Motion Photo splitter for Samsung's Galaxy S7

## Description

Samsung S7 does not provide a way to batch extract photos and/or videos from a Motion Photo. To do it you must do this operation on every picture separately. I wrote small script that allows batch splitting of Motion Photos and saving both video and image file while you upload them to computer. The script works on Linux and OSX.


### How does it work? 

Samsung's Motion Photo format consists of a picture (jpeg) and movie (mp4) merged into a single file. Between them there is a special marker. The script finds the marker and splits it accordingly.
                                                                            
**Requirements** 

- Linux / OSX 
- Python 2.7.x     

                                                                       
                                                                               
## Converting pictures                                                               
                                                                            
                                                                              
### Linux  / OSX

- Place the script in the directory where the images are
- Open the terminal  
  **OSX**: ⌘(Command) + Space, type “Terminal” and then hit “Enter”

  **Linux** : Ctrl + Alt + t
- Run the script  
                                                                                                                                
 ```bash                                                                        
 for p in *.jpg; do                                                            
    python splitter.py ${p}                                                     
  done                                                                          
 ``` 

- Enjoy :coffee: 

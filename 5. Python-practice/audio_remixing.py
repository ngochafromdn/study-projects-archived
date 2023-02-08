"""
These Python functions that implement some basic sound manipulation algorithms, including loop, flipflop, fade, and echo, and new surprising function( namely speed_down_to_up)
name: Nguyen Hoang Ngoc Ha (ID: 210206), Le Thi Hong Ha (ID:210205)
Time : 24 hours
"""
def loop():
    #This function will repeat an imported audio with the number of input time.
    from csc121.audio import read_wav, write_wav
    #Import the function of reading the audio file and writing the audio file
    name=str(input("Enter the name of the audio file:"))
    num=int(input("Enter the number of times repeat the sound clip:"))
    old_audio=read_wav(name)
    new_audio=[]
    for i in range(1,num+1,1):
        new_audio = new_audio + old_audio
    write_wav(new_audio,'looped.wav')
    
def flipflop():
    #This function will wrap the first half and second half of the input audio file.
    from csc121.audio import read_wav, write_wav
    #Import the function of reading the audio file and writing the audio file
    name=str(input("Enter the file name:"))
    old_audio=read_wav(name)
    first_half = old_audio[:len(old_audio)//2]
    second_half = old_audio[len(old_audio)//2:]
    write_wav(second_half+first_half,'flipflopped.wav')
    
    
def fade():
    #This function will make the input audio file gradually fade out. 
    from csc121.audio import read_wav, write_wav
    #Import the function of reading the audio file and writing the audio file
    name=str(input("Enter the file name:"))
    old_audio=read_wav(name)
    #make the input audio file gradually fade out through the loop function.
    for i in range(len(old_audio)):
        old_audio[i]=(1-(i/(len(old_audio)-1)))*old_audio[i]
    write_wav(old_audio,'faded.wav')

def echo():
    from csc121.audio import read_wav, write_wav
    #Import the function of reading the audio file and writing the audio file
    name=str(input("Enter the file name:"))
    old_audio=read_wav(name)
    for i in range(0,len(old_audio),1):
        old_audio[i]=old_audio[i]*0.3
    new_audio= old_audio.copy()
    k=len(old_audio)//8
    for i in range(len(old_audio)):
        if (i+k)<=(len(old_audio)-1):
            new_audio[i+k]=old_audio[i]+old_audio[i+k]
        else:
            new_audio.append(old_audio[i])
    write_wav(new_audio,'echoed.wav')

def speed_down_to_up():
    #This function will make an input audio file move slower and then move again in faster speed.
    from csc121.audio import read_wav, write_wav
    #Import the function of reading the audio file and writing the audio file
    name=str(input("Enter the file name:"))
    old_audio=read_wav(name)
    slow_audio=[]
    fast_audio=[]
    for i in range(0,len(old_audio),1):
            slow_audio.append(old_audio[i])
            slow_audio.append(old_audio[i]*2)
    for i in range(0,len(old_audio),2):
            fast_audio.append(old_audio[i])
    write_wav(slow_audio+new_audio2,'speed_down_to_up.wav')
from random import randrange
c=randrange(12)
#c = 0
def magic(i,x,y,z):
    while c == i :
        
        I1 = input("Change into " + z +" tense\n #########\n " + y +"  \n Answer:" )
        if I1 == x:
            print('Your answer is correct')
            break
        else:
           print('Wrong Answer,Please try again')
           break

magic(0,"I was writing my exam this time yesterday","I will be writing my exam this time tomorrow.","past continuous")
magic(1,"He is waiting for us","He will be waiting for us","present continuous")
magic(2,"I knew this","I know this.","simple past")
magic(3,"He has thought about this","He will have thought about this.","present perfect")
magic(4,"He wants to know more about the job","He wanted to know more about the job.","simple present")
magic(5,"I will be leaving for England tomorrow"," I am leaving for England tomorrow","future continuous")
magic(6,"She didn’t think about that","She hadn’t thought about that.","simple past")
magic(7," He did not accept this proposal","He will not accept this proposal","simple past")
magic(8,"He will not have passed the test","He will not pass the test"," future perfect")
magic(9," I have always wanted to be a scientist","I always wanted to be a scientist.","present perfect")
magic(10,"She did not tolerate that injustice","She will not tolerate this injustice","simple past")
magic(11,"She does not want to go","She did not want to go.","simple present")
#magic(12,"Yes Did","I will be writing my exam this time tomorrow.","past continuous")
#magic(13,"Yes Did","I will be writing my exam this time tomorrow.","past continuous")
#magic(14,"Yes Did","I will be writing my exam this time tomorrow.","past continuous")
#magic(15,"Yes Did","I will be writing my exam this time tomorrow.","past continuous")
#magic(16,"Yes Did","I will be writing my exam this time tomorrow.","past continuous")
#magic(17,"Yes Did","I will be writing my exam this time tomorrow.","past continuous")
#magic(18,"Yes Did","I will be writing my exam this time tomorrow.","past continuous")
#magic(19,"Yes Did","I will be writing my exam this time tomorrow.","past continuous")
#magic(20,"Yes Did","I will be writing my exam this time tomorrow.","past continuous")
#magic(0,"Yes Did","I will be writing my exam this time tomorrow.","past continuous")
#magic(0,"Yes Did","I will be writing my exam this time tomorrow.","past continuous")


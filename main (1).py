#!/usr/bin/env python
# coding: utf-8

# In[2]:


class quiz:

    def __init__(self):
        
        print()
        print('***** Grand  Quiz Master *******')
        self.question_input = []
        self.topic = []
        self.difficulty = []
        self.options = []
        self.answer = {}
        self.question_no = 1
        self.total_score = 0
        self.role()


    def question(self):
        flag = True
        while flag == True:
            question = input('Enter your question:\n')
            self.question_input.append(question)
            tp = input('Enter Section:\n')
            self.topic.append(tp)
            df = input('Enter Difficulty:\n')
            self.difficulty.append(df)
            a = []
            print('Enter the Options:\n')
            for i in range(4):
                a.append(input('Option '+str((i+1))+': '))
            self.options.append(a)
            

            self.answer[self.question_no]=int(input('Enter the correct option: \n'))
            self.question_no += 1
            

            new = input('Press Y to add more questions if not press N to stop:\n')
            if new == 'N' or new == 'n':
                flag = False
                print()
                self.organizer_menu()
            else:
                pass



    def display(self):
        print('Here are the total number of questions:',len(self.question_input))
        print()
        for i in range(len(self.question_input)):
            print('Question: '+self.question_input[i])
            for j in range(len(self.options[i])):
                print(str(j+1)+')'+str(self.options[i][j]))
            print()
        self.role()

    def organizer(self):
        name = input('Enter your Name:\n')
        ID = input('Enter password:\n')
        print()
        print('Hello! Welcome',name)
        print()
        self.organizer_menu()
        
    def organizer_menu(self):
        print('1.Add questions or Create quiz \n 2.Show  questions')
        print('3.Edit questions')
        print('4.create topics \n 5.Delete topic\n 6.Delete quiz \n 7.Exit')
        n=int(input())
        if n==1:
            self.question()
        elif n==2:
            self.display()
        elif n==3:
            self.edit_q()
        elif n==4:
            self.add_topic()
        elif n==5:
            self.delete_topic()
        elif n==6:
            self.delete_quiz()
        elif n==7:
            self.role()
        else:
            print('The mentioned choice does not exist ')
            print('please Enter a valid choice')
            self.organizer_menu()

    def student(self):
        name = input('Enter Name:\n')
        id = int(input('Enter Id:\n'))
        print('Hello',name)
        print('Your Quiz is ready!')
        print()
        self.student_menu()

    def student_menu(self):
        print('1.View Sections avaliable \n2.Take a quiz\n3.Exit')
        f=int(input())
        if f==1:
            self.view_sections()
        elif f==2:
            self.give_test()
        elif f==3:
            self.role()
        else:
            print('The mentioned choice does not exist ')
            print('please Enter a valid choice')
            self.student_menu()

    def add_topic(self):
        q=str(input("please Enter the topic wanted to be added in quiz"))
        self.topic.append(q)
        print('Topic added sucessfully')
        self.organizer_menu()
        
    def delete_topic(self):
        z=str(input('Please enter the topic that needs to be removed'))
        if (z in self.topic):
            self.topic.remove(z)
            print("Topic removed sucessfully!")
            self.organizer_menu()
        else:
            Print("the topic entered does not exist \n Thank you..!")
            self.organizer_menu()
            
    
    def delete_quiz(self):
        c = input('Are you sure you want to delete the quiz press Y for yes N for NO:\n')
        if(c=='Y' or 'y'):
            self.question_input = []
            self.topic = []
            self.difficulty = []
            self.options = []
            self.answer = {}
            print('Quiz got deleted sucessfully')
            print('Total number questions now is', len(self.question_input))
            self.organizer_menu()
        elif( c=='N' or 'n'):
            self.organizer_menu()
            
            
            
        
    
    
    def edit_q(self):
        flag = True
        while flag == True:
            question = input('Enter the question you want to edit:\n')
            if(question in self.question_input):
                i = self.question_input.index(question)
                question2 = input('Please enter the new question:\n')
                self.question_input.insert(i,question2)
                
                tp2 = input('Enter updated Section:\n')
                self.topic.insert(i,tp2)
                df2 = input('Enter updated Difficulty:\n')
                self.difficulty.insert(i,df2)
                a = []
                print('Enter the Options:\n')
                for i in range(4):
                    a.append(input('Option '+str((i+1))+': '))
                self.options.append(a)
            
                self.answer[self.question_no]=int(input('Enter the correct option: \n'))
                self.question_no += 1

                new = input('Press Y to edit nore  questions if not press N to stop:\n')
                if new == 'N' or new == 'n':
                    flag = False
                    print()
                    self.organizer_menu()
                else:
                    pass

            else:
                print('The entered question that want to edit does not exist')
                self.organizer_menu()
                

    
    
    def view_sections(self):
        x=set(self.topic)
        print('Sections:\n',x)
        for i in x:
            print(i)
        print()
        self.student_menu()

    def give_test(self):
        print()
        print('Welcome to your quiz!')
        print('The marking system as follows.')
        print('For easy questions - 5 marks\nFor medium questions - 10 marks\nFor hard questions - 15 marks')
        print('All the best!')
        print()
        score = 0

        for i in range(len(self.question_input)):
            print('Section:'+self.topic[i])
            print('Level of Difficulty:',self.difficulty[i])
            print()
            print(self.question_input[i])
            for j in range(len(self.options[i])):
                print('Option '+str(j+1)+')'+str(self.options[i][j]))
            
            print()
            std_choice = int(input('Enter option number:'))
            print()

            if std_choice == self.answer[i+1]:
                
                if self.difficulty[i] == 'easy':
                    score += 5
                elif self.difficulty[i] == 'medium':
                    score += 10
                elif self.difficulty[i] == 'hard':
                    score += 15
                    
            self.total_score = 0
            for h in self.difficulty:
                if h == 'easy':
                    self.total_score += 5
                elif h == 'medium':
                    self.total_score += 10
                elif h == 'hard':
                    self.total_score += 15


        print('You scored',str(score),'out of',self.total_score)
        print('Thank you for taking the test  :)')
    
    def role(self):
        
        print('\nChoose your role: \n1.Organizer \n2.Student')
        choice = int(input())
        if choice == 1:
            self.organizer()
        elif choice == 2:
            self.student()

a = quiz()


# In[ ]:





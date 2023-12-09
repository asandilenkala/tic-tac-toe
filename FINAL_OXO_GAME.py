import sys
import random
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from LoopThread import*
from GameClient import *

#from OXOTextClient import*
class mywidget(QWidget, GameClient):
    def __init__(self,parent=None):
        QWidget. __init__(self, parent)
        GameClient.__init__(self) 
        self.shape = None
        self.setGeometry(100,100,100,300)
        self.setWindowTitle('THE OXO GAME')  
        
        self.setWindowIcon(QIcon("images.jfif"))#sets the icon for the window
        
        back_pic = QPalette()
        #sets the background picture
        pixmap =  QPixmap("time-lapse-moving-cloud-on-blue-sky-background_4s9ilq19e__F0000.png")#set size of background picture
        pixmap= pixmap.scaledToWidth(2000)
        back_pic.setBrush(QPalette.Background,QBrush(pixmap)) 
        self.setPalette(back_pic)         
        self.setPalette(back_pic)        
        
        #make connection the client and horizontal layout
        self.server_IP = QLabel("SERVER:")
        self.server_IP.setFont(QFont('Times',10,10)) #set font
        self.IP_space  = QLineEdit('localhost')
        self.IP_space.setPlaceholderText("Opponent's IP Address")
        self.conn_button = QPushButton("CONNECT",self)
       
        
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.server_IP)
        hbox.addWidget(self.IP_space)
        hbox.addWidget(self.conn_button)
        self.hbox_widget0 = QWidget()
        self.hbox_widget0.setLayout(hbox) 
        
        #make board with positions and make layout
        #zero ,1st, 2nd position
        pixmap = QPixmap("blank.gif")
        pixmap= pixmap.scaledToWidth(50)
        self.position0 = QLabel()
        self.position0.setPixmap(pixmap)         
        pixmap = QPixmap("blank.gif")
        pixmap= pixmap.scaledToWidth(50)
        self.position1 = QLabel()
        self.position1.setPixmap(pixmap)         
        pixmap = QPixmap("blank.gif")
        pixmap= pixmap.scaledToWidth(50)
        self.position2 = QLabel()
        self.position2.setPixmap(pixmap)         
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.position0)
        hbox.addWidget(self.position1)
        hbox.addWidget(self.position2)
        self.hbox_widget2 = QWidget()
        self.hbox_widget2.setLayout(hbox) 
        #3rd,4th,5th positions
        pixmap = QPixmap("blank.gif")
        pixmap= pixmap.scaledToWidth(50)
        self.position3 = QLabel()
        self.position3.setPixmap(pixmap)         
        pixmap = QPixmap("blank.gif")
        pixmap= pixmap.scaledToWidth(50)
        self.position4 = QLabel()
        self.position4.setPixmap(pixmap)         
        pixmap = QPixmap("blank.gif")
        pixmap= pixmap.scaledToWidth(50)
        self.position5 = QLabel()
        self.position5 .setPixmap(pixmap)         
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.position3)
        hbox.addWidget(self.position4)
        hbox.addWidget(self.position5)
        self.hbox_widget3 = QWidget()
        self.hbox_widget3.setLayout(hbox) 
        
        self.tool = QLabel()
        
        #6th,7th,8th positions
        self.score = QLabel('')
        self.score.setFont(QFont('Courier',20,2))
        self.score_2 = QLabel('')
        self.score_2.setFont(QFont('Courier',20,2))        
        # adds the blank pictures for the game board
        pixmap = QPixmap("blank.gif")
        pixmap= pixmap.scaledToWidth(50)
        self.position6 = QLabel()
        self.position6.setPixmap(pixmap)        
        pixmap = QPixmap("blank.gif")
        pixmap= pixmap.scaledToWidth(50)
        
        self.position7 = QLabel()
        self.position7.setPixmap(pixmap)         
        pixmap = QPixmap("blank.gif")
        pixmap= pixmap.scaledToWidth(50)
        self.position8 = QLabel()
        self.position8.setPixmap(pixmap)        
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.position6)
        hbox.addWidget(self.position7)
        hbox.addWidget(self.position8)
        self.hbox_widget4 = QWidget()
        self.hbox_widget4.setLayout(hbox) 
        
        #make positions vertical from each other
        self.board = QLabel( "    GAME BOARD:")
        self.board.setFont(QFont('Times',12,2))
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.board)
        vbox.addWidget(self.hbox_widget2)
        vbox.addWidget(self.hbox_widget3)
        vbox.addWidget(self.hbox_widget4)
        vbox.addWidget(self.tool)
        self.vbox_widget_positions = QWidget()
        self.vbox_widget_positions.setLayout(vbox)
        #make my shape label label horintal with the shape
        self.iput_move = QLabel('             POSITION KEY-BOARD:')
        self.iput_move.setFont(QFont('Times',11,1))
        #self.input_move_space = QLineEdit()
        
        #buttons that be used to play OXO GAME instead device keyboard
        self.lul = QPushButton('0')
        self.lul1 = QPushButton('1')
        self.lul2 = QPushButton('2')
        self.lul3 = QPushButton('3')
        self.lul4 = QPushButton('4')
        self.lul5 = QPushButton('5')
        self.lul6 = QPushButton('6')
        self.lul7 = QPushButton('7')
        self.lul8 = QPushButton('8')
        # makes the first row of the blank pictures for the Game Board
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.lul)
        hbox.addWidget(self.lul1)
        hbox.addWidget(self.lul2)
        self.sh = QWidget()
        self.sh.setLayout(hbox)        
       # makes the second row of the blank pictures for the Game Board
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.lul3)
        hbox.addWidget(self.lul4)
        hbox.addWidget(self.lul5)
        self.ape = QWidget()
        self.ape.setLayout(hbox)        
        # makes the third row of the blank pictures for the Game Board
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.lul6)
        hbox.addWidget(self.lul7)
        hbox.addWidget(self.lul8)
        self.la = QWidget()
        self.la.setLayout(hbox)        
        
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.sh)
        vbox.addWidget(self.ape)
        vbox.addWidget(self.la)
        self.kok = QWidget()
        self.kok.setLayout(vbox)
        
        hbox = QVBoxLayout(self)
        hbox.addWidget(self.iput_move)
        hbox.addWidget(self.kok)
        self.move_space = QWidget()
        self.move_space.setLayout(hbox) 
        
        #label of shape of each client and sets the font
        self.shape = QLabel("MY SHAPE:")
        self.score_1 = QLabel('SCORE O:')
        self.score_2 = QLabel('SCORE X:')
        self.score_1_X = QLabel('')
        self.score_2_O = QLabel('')
        self.score_1_X.setFont(QFont('Times',12,1))
        self.score_2_O.setFont(QFont('Times',12,1))        
        self.shape.setFont(QFont('Times',12,1))
        self.score_1.setFont(QFont('Times',12,1))
        self.score_2.setFont(QFont('Times',12,1))
        self.lbl = QLabel(self)
       # makes the shape label and the player shape  vertically 
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.shape)
        vbox.addWidget(self.lbl)
        self.B_10 = QWidget()
        self.B_10.setLayout(vbox)
        #makes the label of the scores for both users vertically
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.score_1)
        vbox.addWidget(self.score_2)
        self.C_10 = QWidget()
        self.C_10.setLayout(vbox)
        #makes the scores for both users vertically
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.score_1_X)
        vbox.addWidget(self.score_2_O)
        self.D_10 = QWidget()
        self.D_10.setLayout(vbox)        
        #makes prints the above widgets horizontally
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.B_10)
        hbox.addWidget(self.C_10)
        hbox.addWidget(self.D_10)
        self.E_10 = QWidget()
        self.E_10.setLayout(hbox)        
        # makes the scores
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.move_space)
        vbox.addWidget(self.E_10) 
        self.shape_label = QWidget()
        self.shape_label.setLayout(vbox) 
        #make shape of each client and layout positions & shape hozintally
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.vbox_widget_positions)
        hbox.addWidget(self.shape_label)
        self.hbox_widget5 = QWidget()
        self.hbox_widget5.setLayout(hbox)  
        #make textedit to give appropriate messages
        self.message_label = QLabel(" MESSAGES:",self)
        self.message_label.setFont(QFont('Times',12,2))
        self.text_dit      = QTextEdit()
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.message_label)
        vbox.addWidget(self.text_dit )
        self.vbox_widget_messages = QWidget()
        self.vbox_widget_messages.setLayout(vbox)
        #make combo for play again ,make exit button  and make vertical layout
        self.play_again_label = QLabel("PLAY AGAIN:",self)
        self.play_again_label.setFont(QFont('Times',11,2))
        #combo for play again
        combo = ['YES','NO'] 
        self.combo = QComboBox(self)
        self.combo.setEnabled(False)
        for x in combo:
            self.combo.addItem(x)
        self.combo.activated.connect(self.combo_box)#connect close signal with combo box
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.play_again_label)
        hbox.addWidget(self.combo)
        self.play_again= QWidget()
        self.play_again.setLayout(hbox)
        
        self.exit_button = QPushButton("EXIT",self)
        self.exit_button.clicked.connect(self.exit_game)#connect exit button with  exit fuction to close window if exit is clicked
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.play_again)
        vbox.addWidget(self.exit_button )
        self.play_again_exit = QWidget()
        self.play_again_exit.setLayout(vbox) 
        #make play again combo, exit button and text edit horizontal from each other
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.vbox_widget_messages)
        hbox.addWidget(self.play_again_exit)
        self.hbox_widget6 = QWidget()
        self.hbox_widget6.setLayout(hbox) 
        #make all the layout in order and display them 
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.hbox_widget0)
        vbox.addWidget(self.hbox_widget5)
        vbox.addWidget(self.hbox_widget6)
        self.hbox_widget7 = QWidget()    
        self.setLayout(vbox)
         
        #self.game = OXOGameClient()        
        #creat a thread
        self.thread = LoopThread()
        self.thread.game_signal.connect(self.loop_slot) # connect signals to slots
        self.conn_button.clicked.connect(self.conn)                  #connect close signal with the connect  button
        
        self.lul.clicked.connect(self.pos_0)
        self.lul1.clicked.connect(self.pos_1)
        self.lul2.clicked.connect(self.pos_2)#connect the with the inputed move
        self.lul3.clicked.connect(self.pos_3)    
        self.lul4.clicked.connect(self.pos_4)#connect the with the inputed move
        self.lul5.clicked.connect(self.pos_5)
        self.lul6.clicked.connect(self.pos_6)#connect the with the inputed move
        self.lul7.clicked.connect(self.pos_7)    
        self.lul8.clicked.connect(self.pos_8)
        
        self.cross = QPixmap("cross.gif")
        self.nought = QPixmap("nought.gif")
        self.blank = QPixmap("blank.gif")
        self.icon_O = self.nought  
        self.icon_X = self.cross
        self.positions = ["0","1","2","3","4","5","6","7","8"] #list for postions
        
        self.O_score = 0
        self.X_score = 0
        
    def write_to_edit(self,msg): #Function to handle messages
        self.shape = msg[-1]
        if msg[:msg.find(",")] == "new game" and self.shape == 'O':
            self.icon_O = self.nought
            self.lbl.setPixmap(self.icon_O)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append(msg[:8] + "\n")
            self.score_1_X.setText("{0} ".format((self.O_score)))
            self.score_2_O.setText("{0} ".format((self.X_score)))
            
        elif msg[:msg.find(",")] == "new game" and self.shape== 'X': 
            self.icon_X = self.cross
            self.lbl.setPixmap(self.icon_X)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append(msg[:8] + "\n") 
            self.score_2_O.setText("{0} ".format((self.X_score)))
            self.score_1_X.setText("{0} ".format((self.O_score)))
            
        elif msg == 'your move':   # tell each it's his/her move
            self.conn_button.setEnabled(False)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append(msg + "\n") 
            self.combo.setEnabled(False)
            self.lul.setEnabled(True)
            self.lul1.setEnabled(True)
            self.lul2.setEnabled(True)
            self.lul3.setEnabled(True)
            self.lul4.setEnabled(True)
            self.lul5.setEnabled(True)
            self.lul6.setEnabled(True)
            self.lul7.setEnabled(True)
            self.lul8.setEnabled(True)
            
        elif msg == "opponents move":# tell each it's oppenent move
            self.conn_button.setEnabled(False)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append(msg + "\n")
            self.combo.setEnabled(False)
            self.lul.setEnabled(False)
            self.lul1.setEnabled(False)
            self.lul2.setEnabled(False)
            self.lul3.setEnabled(False)
            self.lul4.setEnabled(False)
            self.lul5.setEnabled(False)
            self.lul6.setEnabled(False)
            self.lul7.setEnabled(False)
            self.lul8.setEnabled(False)
            
        elif msg == "invalid move": #invalid and write invalid move
            self.conn_button.setEnabled(False)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append(msg + "\n")
            
        elif msg[:msg.find(",")] == "game over": #check game over            
            self.conn_button.setEnabled(False)
            if msg[-1] == 'X' or msg[-1] == 'O':
                self.text_dit.setFontPointSize(16)
                redColor = QColor(255, 0, 0)
                self.text_dit.setTextColor(redColor)
                self.text_dit.append('***Game over, the winner is ' + (msg[-1])+ "***" + "\n") 
                self.text_dit.setFontPointSize(12)
                blackColor = QColor(0, 0, 0)
                self.text_dit.setTextColor(blackColor)                
                if msg[-1] == "X":
                    self.X_score +=1
                    
                elif msg[-1] == "O":
                    self.O_score +=1
                
            else:
                self.text_dit.setFontPointSize(12)
                self.text_dit.append("Game over, It's a tie!" + "\n")
                
            self.score_1_X.setText("{0} ".format((self.O_score))) 
            self.score_2_O.setText("{0} ".format((self.X_score)))            
                
        elif msg == 'play again':
            self.conn_button.setEnabled(False)
            self.combo.setEnabled(True)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append("Click YES if you want to play again!!!" + "\n")
             #get answer from user
            #self.combo.activated.connect(self.ans)
            
        elif msg == 'exit game': #play again game or exist game
            self.conn_button.setEnabled(False)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append("Press Exit button to Exit game!!!" + "\n")
                                   
                
        elif msg[:msg.find(",")]=="valid move": #check valid move then apply method(play the game)
            self.conn_button.setEnabled(False)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append(msg[:10] + '\n')
            pixmap_x = QPixmap('cross.gif')
            pixmap_o = QPixmap('nought.gif')
            position =msg.split(",")[2]
            self.shape = msg[-3]
            #put shape on position if the position button is clicked
            if position=='0' and self.shape=='X':
                self.position0.setPixmap(pixmap_x)
            elif position=='0' and self.shape=='O':
                self.position0.setPixmap(pixmap_o)
                
            elif position=='1' and self.shape=='X':
                self.position1.setPixmap(pixmap_x)
            elif position =='1' and self.shape=='O':
                self.position1.setPixmap(pixmap_o)
                
            elif position=='2' and self.shape=='X':
                self.position2.setPixmap(pixmap_x)
            elif position=='2' and self.shape=='O':
                self.position2.setPixmap( pixmap_o)   
                
            elif position=='3' and self.shape=='X':
                self.position3.setPixmap(pixmap_x)
            elif position=='3' and self.shape=='O':
                self.position3.setPixmap(pixmap_o)
                
            elif position=='4' and self.shape=='X':
                self.position4.setPixmap(pixmap_x)
            elif position =='4' and self.shape=='O':
                self.position4.setPixmap(pixmap_o) 
            
            elif position=='5' and self.shape=='X':
                self.position5.setPixmap( pixmap_x)
            elif position=='5' and self.shape=='O':
                self.position5.setPixmap(pixmap_o)
                
            elif position=='6' and self.shape=='X':
                self.position6.setPixmap(pixmap_x)
            elif position=='6' and self.shape=='O':
                self.position6.setPixmap(pixmap_o)   
                
            elif position=='7' and self.shape=='X':
                self.position7.setPixmap(pixmap_x)
            elif position=='7' and self.shape=='O':
                self.position7.setPixmap(pixmap_o)
                
            elif position=='8' and self.shape=='X':
                self.position8.setPixmap(pixmap_x)
            elif position =='8' and self.shape=='O':
                self.position8.setPixmap(pixmap_o)
            
    def pos_0(self): #fuction for  position zero
        try: 
            self.thread.send_message(self.positions[0])
        except Exception as r:
            print(r)
            
    def pos_1(self): #fuction for  position 1
        try: 
            self.thread.send_message(self.positions[1])
        except Exception as r:
            print(r) 
            
    def pos_2(self): #fuction for  position 2
        try: 
            self.thread.send_message(self.positions[2])
        except Exception as r:
            print(r)
            
    def pos_3(self): #fuction for  position 3
        try: 
            self.thread.send_message(self.positions[3])
        except Exception as r:
            print(r)
            
    def pos_4(self): #fuction for  position 4
        try: 
            self.thread.send_message(self.positions[4])
        except Exception as r:
            print(r) 
            
    def pos_5(self): #fuction for  position 5
        try: 
            self.thread.send_message(self.positions[5])
        except Exception as r:
            print(r) 
            
    def pos_6(self): #fuction for  position 6
        try: 
            self.thread.send_message(self.positions[6])
        except Exception as r:
            print(r)
            
    def pos_7(self): #fuction for  position 7
        try: 
            self.thread.send_message(self.positions[7])
        except Exception as r:
            print(r)
            
    def pos_8(self): #fuction for  position 8
        try: 
            self.thread.send_message(self.positions[8])
        except Exception as r:
            print(r)          
           
    def loop_slot(self, msg): # slot which handles signal from thread
        self.write_to_edit(msg) 
        
    #fuction to connect
    def conn(self):      
        try:
            self.thread.connect_(self.IP_space.displayText())  #connecting to server
            self.thread.start()                                #starting thread for play loop to begin
            self.text_dit.setFontPointSize(12)
            self.text_dit.append("Connected to Client")       #set messege on text edit when you are connected
        except Exception as t:
            print(t) 
        
# make fuction print out after clicking  combo box
    def combo_box(self):
        self.conn_button.setEnabled(False)
        self.ans = self.combo.currentText() 
        if self.ans == 'YES': #if answer is yes , clear board and text edit an d write new game on text edit 
                self.position0.setPixmap(self.blank)
                self.position1.setPixmap(self.blank)
                self.position2.setPixmap(self.blank)
                self.position3.setPixmap(self.blank)
                self.position4.setPixmap(self.blank)
                self.position5.setPixmap(self.blank)
                self.position6.setPixmap(self.blank)
                self.position7.setPixmap(self.blank)
                self.position8.setPixmap(self.blank)
                self.text_dit.clear()
                self.text_dit.setFontPointSize(12)
                self.text_dit.append('New game with same opponent.' + "\n")
                self.thread.send_message("y")
         
         # If a user chooses NO in the combobox     
        elif self.ans == 'NO':
            self.conn_button.setEnabled(False)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append('Game ended!!!!' + "\n")
            self.thread.send_message("n")
            
    #exit  fuction
    def exit_game(self):
        self.close()
           
def main():
    app = QApplication(sys.argv)
    x = mywidget()
    x.show()
    sys.exit(app.exec_())       
main()
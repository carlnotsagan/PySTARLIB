# Copyright (c) 2016, Carl Fields cef@asu.edu

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import subprocess,os

def starlib_search_chapter_1(a_in, a_out,minus,rate):
    possible_reactions = []
    possible_reactions_line_nums = []
    final_reaction = []
    final_line_num = []
    
    if a_in == 'h2':
        a_in = 'd'
    if a_in == 'neut':
        a_in = 'n'
    if a_out == 'neut':
        a_out = 'n'
        
    # process as a chapter 1 weak reaction
    #############################################
    all_nuclei = ("1",str(a_in),str(a_out))
    file = open('starlib_v5.dat', 'r')
    for num,line in enumerate(file,1):
        if all(s in line for s in all_nuclei):
            possible_reactions.append(line)
            possible_reactions_line_nums.append(num)
                
    index = len(possible_reactions)

    for i in range(index):
        test = possible_reactions[i]
        if "1" in test[:2]:
            final_reaction.append(possible_reactions[i])  
            final_line_num.append(possible_reactions_line_nums[i]) 
            
    if a_in == 'd':
        a_in = 'h2'
    if a_in == 'n':
        a_in = 'neut'
    if a_out == 'n':
        a_out = 'neut'
        
    if not final_line_num:
        print 'Sorry, no rate found for r_'+str(a_in)+'_wk_'+str(a_out)+''
        failed_rates.append(rate)       
        return
   
    file = open('starlib_v5.dat', 'r')
    
    if minus == "True":
        fo = open('./starlib_raw_rates/r_'+str(a_in)+'_wk-minus_'+str(a_out)+'.txt', 'w+')
        for i, text in enumerate(file):
            if i > int(final_line_num[0]) - 2 and i < int(final_line_num[0]) + 60:
                fo.write(text)
            else:
                pass
            
        fo.close()
        
    else:
        fo = open('./starlib_raw_rates/r_'+str(a_in)+'_wk_'+str(a_out)+'.txt', 'w+')
        for i, text in enumerate(file):
            if i > int(final_line_num[0]) - 2 and i < int(final_line_num[0]) + 60:
                fo.write(text)
            else:
                pass
            
        fo.close()
    
    return 

def starlib_search_chapter_4(a_in, interaction, a_out,rate):
    possible_reactions = []
    possible_reactions_line_nums = []
    final_reaction = []
    final_line_num = []
    
    if a_in == 'h2':
        a_in = 'd'
    if a_in == 'neut':
        a_in = 'n'
    if a_out == 'neut':
        a_out = 'n'
        
    # process as a chapter 4 a_in(alpha,gamma)a_out reaction
    #############################################
    if str(interaction) == 'he4':
        all_nuclei = ("he4","4",str(a_in),str(a_out))
        file = open('starlib_v5.dat', 'r')
        for num,line in enumerate(file,1):
            if all(s in line for s in all_nuclei):
                possible_reactions.append(line)
                possible_reactions_line_nums.append(num)
                
        index = len(possible_reactions)
    
        for i in range(index):
            test = possible_reactions[i]
            if "4" in test[:2]:
                final_reaction.append(possible_reactions[i])  
                final_line_num.append(possible_reactions_line_nums[i]) 
                       
        if a_in == 'd':
            a_in = 'h2'
        if a_in == 'n':
            a_in = 'neut'
        if a_out == 'n':
            a_out = 'neut'
                
        if not final_line_num:
            print 'Sorry, no rate found for r_'+str(a_in)+'_ag_'+str(a_out)+''
            failed_rates.append(rate)
            return
                
        file = open('starlib_v5.dat', 'r')       
        fo = open('./starlib_raw_rates/r_'+str(a_in)+'_ag_'+str(a_out)+'.txt', 'w+')
        for i, text in enumerate(file):
            if i > int(final_line_num[0]) - 2 and i < int(final_line_num[0]) + 60:
                fo.write(text)
            else:
                pass
            
        fo.close()
        
    # process as a chapter 4 a_in(p,gamma)a_out reaction
    #############################################
    if str(interaction) == 'p':
        all_nuclei = ("p","4",str(a_in),str(a_out))
        file = open('starlib_v5.dat', 'r')
        for num,line in enumerate(file,1):
            if all(s in line for s in all_nuclei):
                possible_reactions.append(line)
                possible_reactions_line_nums.append(num)
                
        index = len(possible_reactions)
    
        for i in range(index):
            test = possible_reactions[i]
            if "4" in test[:2]:
                final_reaction.append(possible_reactions[i])  
                final_line_num.append(possible_reactions_line_nums[i]) 
                                
        if a_in == 'd':
            a_in = 'h2'
        if a_in == 'n':
            a_in = 'neut'
        if a_out == 'n':
            a_out = 'neut'
                
        if not final_line_num:
            print 'Sorry, no rate found for r_'+str(a_in)+'_pg_'+str(a_out)+''
            failed_rates.append(rate)
            return
            
        file = open('starlib_v5.dat', 'r')       
        fo = open('./starlib_raw_rates/r_'+str(a_in)+'_pg_'+str(a_out)+'.txt', 'w+')
        for i, text in enumerate(file):
            if i > int(final_line_num[0]) - 2 and i < int(final_line_num[0]) + 60:
                fo.write(text)
            else:
                pass
            
        fo.close()
        
    # process as a chapter 4 a_in(n,gamma)a_out reaction
    #############################################
    if str(interaction) == 'n':
        all_nuclei = ("n","4",str(a_in),str(a_out))
        file = open('starlib_v5.dat', 'r')
        for num,line in enumerate(file,1):
            if all(s in line for s in all_nuclei):
                possible_reactions.append(line)
                possible_reactions_line_nums.append(num)
                
        index = len(possible_reactions)
    
        for i in range(index):
            test = possible_reactions[i]
            if "4" in test[:2]:
                final_reaction.append(possible_reactions[i])  
                final_line_num.append(possible_reactions_line_nums[i]) 
                                       
        if a_in == 'd':
            a_in = 'h2'
        if a_in == 'n':
            a_in = 'neut'
        if a_out == 'n':
            a_out = 'neut'
                
        if not final_line_num:
            print 'Sorry, no rate found for r_'+str(a_in)+'_ng_'+str(a_out)+''
            failed_rates.append(rate)
            return
                
            
        file = open('starlib_v5.dat', 'r')       
        fo = open('./starlib_raw_rates/r_'+str(a_in)+'_ng_'+str(a_out)+'.txt', 'w+')
        for i, text in enumerate(file):
            if i > int(final_line_num[0]) - 2 and i < int(final_line_num[0]) + 60:
                fo.write(text)
            else:
                pass
            
        fo.close()

    
    return 
    
def starlib_search_chapter_5(a_in, interaction, a_out,rate):
    possible_reactions = []
    possible_reactions_line_nums = []
    final_reaction = []
    final_line_num = []
    
    if a_in == 'h2':
        a_in = 'd'
    if a_in == 'neut':
        a_in = 'n'
    if a_out == 'neut':
        a_out = 'n'
        
    # process as a chapter 5 a_in(alpha,p)a_out reaction
    #############################################
    if str(interaction) == 'ap':
        all_nuclei = ("he4","p","5",str(a_in),str(a_out))
        file = open('starlib_v5.dat', 'r')
        for num,line in enumerate(file,1):
            if all(s in line for s in all_nuclei):
                if "v " in line:
                    pass
                else:
                    possible_reactions.append(line)
                    possible_reactions_line_nums.append(num)
                
        index = len(possible_reactions)
    
        for i in range(index):
            test = possible_reactions[i]
            if "5" in test[:2]:
                final_reaction.append(possible_reactions[i])  
                final_line_num.append(possible_reactions_line_nums[i])                
                        
        if a_in == 'd':
            a_in = 'h2'
        if a_in == 'n':
            a_in = 'neut'
        if a_out == 'n':
            a_out = 'neut'
                
        if not final_line_num:
            print 'Sorry, no rate found for r_'+str(a_in)+'_ap_'+str(a_out)+''
            failed_rates.append(rate)
            return
                
                
        file = open('starlib_v5.dat', 'r')       
        fo = open('./starlib_raw_rates/r_'+str(a_in)+'_ap_'+str(a_out)+'.txt', 'w+')
        for i, text in enumerate(file):
            if i > int(final_line_num[0]) - 2 and i < int(final_line_num[0]) + 60:
                fo.write(text)
            else:
                pass
            
        fo.close()
        
        
    # process as a chapter 5 a_in(p,alpha)a_out reaction
    #############################################
    if str(interaction) == 'pa':
        all_nuclei = ("he4","p","5",str(a_in),str(a_out))
        file = open('starlib_v5.dat', 'r')
        for num,line in enumerate(file,1):
            if all(s in line for s in all_nuclei):
                if "v " in line:
                    pass
                else:
                    possible_reactions.append(line)
                    possible_reactions_line_nums.append(num)
                
        index = len(possible_reactions)
    
        for i in range(index):
            test = possible_reactions[i]
            if "5" in test[:2]:
                final_reaction.append(possible_reactions[i])  
                final_line_num.append(possible_reactions_line_nums[i]) 
                                       
        if a_in == 'd':
            a_in = 'h2'
        if a_in == 'n':
            a_in = 'neut'
        if a_out == 'n':
            a_out = 'neut'
                
        if not final_line_num:
            print 'Sorry, no rate found for r_'+str(a_in)+'_pa_'+str(a_out)+''
            failed_rates.append(rate)
            return
                
        file = open('starlib_v5.dat', 'r')       
        fo = open('./starlib_raw_rates/r_'+str(a_in)+'_pa_'+str(a_out)+'.txt', 'w+')
        for i, text in enumerate(file):
            if i > int(final_line_num[0]) - 2 and i < int(final_line_num[0]) + 60:
                fo.write(text)
            else:
                pass
            
        fo.close()
        
    # process as a chapter 5 a_in(alpha,n)a_out reaction
    #############################################
    if str(interaction) == 'an':
        all_nuclei = ("he4","n","5",str(a_in),str(a_out))
        file = open('starlib_v5.dat', 'r')
        for num,line in enumerate(file,1):
            if all(s in line for s in all_nuclei):
                if "v " in line:
                    pass
                else:
                    possible_reactions.append(line)
                    possible_reactions_line_nums.append(num)
                
        index = len(possible_reactions)
    
        for i in range(index):
            test = possible_reactions[i]
            if "5" in test[:2]:
                final_reaction.append(possible_reactions[i])  
                final_line_num.append(possible_reactions_line_nums[i]) 
                                        
        if a_in == 'd':
            a_in = 'h2'
        if a_in == 'n':
            a_in = 'neut'
        if a_out == 'n':
            a_out = 'neut'
                       
        if not final_line_num:
            print 'Sorry, no rate found for r_'+str(a_in)+'_an_'+str(a_out)+''
            failed_rates.append(rate)
            return
            
        file = open('starlib_v5.dat', 'r')       
        fo = open('./starlib_raw_rates/r_'+str(a_in)+'_an_'+str(a_out)+'.txt', 'w+')
        for i, text in enumerate(file):
            if i > int(final_line_num[0]) - 2 and i < int(final_line_num[0]) + 60:
                fo.write(text)
            else:
                pass
            
        fo.close()
 
    # process as a chapter 5 a_in(n,alpha)a_out reaction
    #############################################
    if str(interaction) == 'na':
        all_nuclei = ("he4","n","5",str(a_in),str(a_out))
        file = open('starlib_v5.dat', 'r')
        for num,line in enumerate(file,1):
            if all(s in line for s in all_nuclei):
                if "v " in line:
                    pass
                else:
                    possible_reactions.append(line)
                    possible_reactions_line_nums.append(num)
                
        index = len(possible_reactions)
    
        for i in range(index):
            test = possible_reactions[i]
            if "5" in test[:2]:
                final_reaction.append(possible_reactions[i])  
                final_line_num.append(possible_reactions_line_nums[i])                
                        
        if a_in == 'd':
            a_in = 'h2'
        if a_in == 'n':
            a_in = 'neut'
        if a_out == 'n':
            a_out = 'neut'
                
        if not final_line_num:
            print 'Sorry, no rate found for r_'+str(a_in)+'_na_'+str(a_out)+''
            failed_rates.append(rate)
            return
            
        file = open('starlib_v5.dat', 'r')       
        fo = open('./starlib_raw_rates/r_'+str(a_in)+'_na_'+str(a_out)+'.txt', 'w+')
        for i, text in enumerate(file):
            if i > int(final_line_num[0]) - 2 and i < int(final_line_num[0]) + 60:
                fo.write(text)
            else:
                pass
            
        fo.close()
             
             
    # process as a chapter 5 a_in(p,n)a_out reaction
    #############################################
    if str(interaction) == 'pn':
        all_nuclei = ("n","p","5",str(a_in),str(a_out))
        file = open('starlib_v5.dat', 'r')
        for num,line in enumerate(file,1):
            if all(s in line for s in all_nuclei):
                if "v " in line:
                    pass
                else:
                    possible_reactions.append(line)
                    possible_reactions_line_nums.append(num)

        index = len(possible_reactions)
    
        for i in range(index):
            test = possible_reactions[i]
            if "5" in test[:2]:
                final_reaction.append(possible_reactions[i])  
                final_line_num.append(possible_reactions_line_nums[i])              
                        
        if a_in == 'd':
            a_in = 'h2'
        if a_in == 'n':
            a_in = 'neut'
        if a_out == 'n':
            a_out = 'neut'
                
        if not final_line_num:
            print 'Sorry, no rate found for r_'+str(a_in)+'_pn_'+str(a_out)+''
            failed_rates.append(rate)
            return
            
        file = open('starlib_v5.dat', 'r')       
        fo = open('./starlib_raw_rates/r_'+str(a_in)+'_pn_'+str(a_out)+'.txt', 'w+')
        for i, text in enumerate(file):
            if i > int(final_line_num[0]) - 2 and i < int(final_line_num[0]) + 60:
                fo.write(text)
            else:
                pass
            
        fo.close()
        
        
    # process as a chapter 5 a_in(n,p)a_out reaction
    #############################################
    if str(interaction) == 'np':
        all_nuclei = ("n","p","5",str(a_in),str(a_out))
        file = open('starlib_v5.dat', 'r')
        for num,line in enumerate(file,1):
            if all(s in line for s in all_nuclei):
                if "v " in line:
                    pass
                else:
                    possible_reactions.append(line)
                    possible_reactions_line_nums.append(num)

        index = len(possible_reactions)
    
        for i in range(index):
            test = possible_reactions[i]
            if "5" in test[:2]:
                final_reaction.append(possible_reactions[i])  
                final_line_num.append(possible_reactions_line_nums[i])                 
                        
        if a_in == 'd':
            a_in = 'h2'
        if a_in == 'n':
            a_in = 'neut'
        if a_out == 'n':
            a_out = 'neut'
                
        if not final_line_num:
            print 'Sorry, no rate found for r_'+str(a_in)+'_np_'+str(a_out)+''
            failed_rates.append(rate)
            return

        file = open('starlib_v5.dat', 'r')       
        fo = open('./starlib_raw_rates/r_'+str(a_in)+'_np_'+str(a_out)+'.txt', 'w+')
        for i, text in enumerate(file):
            if i > int(final_line_num[0]) - 2 and i < int(final_line_num[0]) + 60:
                fo.write(text)
            else:
                pass
            
        fo.close()

    
    return 
    
failed_rates = []

def extract_rates():
    
    scrubbed_data = []
    only_forward_rates = []
    only_forward_rate_labels = []

    subprocess.call(['./get_rates.sh']) 
    
    with open('rate_list_w_q_values.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('rate_list_w_q_values_trimmed.txt', 'w') as fout:
        fout.writelines(data[1:])    
    with open("rate_list_w_q_values_trimmed.txt") as f:
        raw_list_w_q_values = [line.rstrip() for line in f]
    
    print "Number of reactions in list:",len(raw_list_w_q_values)-1
        
    for i in range(len(raw_list_w_q_values)):
        reverse_rate_hooks = (" -","photo","_to_","ec")
        if any(x in raw_list_w_q_values[i] for x in reverse_rate_hooks): 
            pass 
        else:
            only_forward_rates.append(raw_list_w_q_values[i])
        
    for i in range (len(only_forward_rates)):
        only_forward_rate_labels.append(only_forward_rates[i].split())
    
    for i in range (0,len(only_forward_rate_labels)-1):
	    scrubbed_data.append(only_forward_rate_labels[i][0])

    print "Number of reactions in scrubbed list:",len(scrubbed_data)

    os.remove('rate_list_w_q_values.txt')
    os.remove('rate_list_w_q_values_trimmed.txt')
      
    for i in range(len(scrubbed_data)):
        all_chapter4_interactions = ("ag","pg","ng")
        all_chapter5_interactions = ("pn","an","ap","np","na","pa")
    
        a = scrubbed_data[i]
        
        # weak interactions 
        if "_wk" in a:
                
            isotope_a_in = a[2:5]
            if "_" in isotope_a_in: 
                isotope_a_in = a[2:4]
            if "_" not in a[2:6]: 
                isotope_a_in = a[2:6]       
            
            # identify output isotope
            isotope_a_out = a[len(a)-3:len(a)]
            if "_" in isotope_a_out: 
                isotope_a_out = a[len(a)-2:len(a)]         
            if "_" not in a[len(a)-4:len(a)]: 
	            isotope_a_out = a[len(a)-4:len(a)]

            #check if minus interaction
            if "wk-minus" in a:
                minus = 'True'
            else:
                minus = 'False'
                
            starlib_search_chapter_1(isotope_a_in,isotope_a_out,minus,scrubbed_data[i])
                      
    
        # check for interaction type of chapter 4
        if any(x in a for x in all_chapter4_interactions):    
        
            # identify input isotope
            isotope_a_in = a[2:5]
            if "_" in isotope_a_in: 
                isotope_a_in = a[2:4]
            if "_" not in a[2:6]: 
                isotope_a_in = a[2:6]       
        
            # deteremine interaction 
            if "_ag_" in a:
                capture = "he4"
    	        interaction = "ag"
            if "_pg_" in a:
                capture = "p"
                interaction = "pg"
            if "_ng_" in a:
                capture = "n"
                interaction = "ng"
                
            # identify output isotope
            isotope_a_out = a[len(a)-3:len(a)]
            if "_" in isotope_a_out: 
                isotope_a_out = a[len(a)-2:len(a)]
            if "_" not in a[len(a)-4:len(a)]: 
                isotope_a_out = a[len(a)-4:len(a)]       

            starlib_search_chapter_4(isotope_a_in, capture, isotope_a_out,scrubbed_data[i])
        
        
        # check interaction type of chapter 5
        if any(x in a for x in all_chapter5_interactions):  
            
            # identify input isotope
            isotope_a_in = a[2:5]
            if "_" in isotope_a_in: 
                isotope_a_in = a[2:4]
            if "_" not in a[2:6]: 
                isotope_a_in = a[2:6]       
        
            # deteremine interaction 
            if "_an_" in a:
                capture = "he4"
                interaction = "an"
            if "_ap_" in a:
                capture = "he4"
                interaction = "ap"
            if "_pn_" in a:
                capture = "p"
                interaction = "pn"
            if "_na_" in a:
                capture = "n"
                interaction = "na"
            if "_pa_" in a:
                capture = "p"
                interaction = "pa"
            if "_np_" in a:
                capture = "n"
                interaction = "np"
                
            # identify output isotope
            isotope_a_out = a[len(a)-3:len(a)]
            if "_" in isotope_a_out: 
                isotope_a_out = a[len(a)-2:len(a)]
            if "_" not in a[len(a)-4:len(a)]: 
                isotope_a_out = a[len(a)-4:len(a)]       

            starlib_search_chapter_5(isotope_a_in, interaction, isotope_a_out,scrubbed_data[i])
           
    ratelist = open('./starlib_raw_rates/rates_list.txt', 'w+')
    for i in range(len(scrubbed_data)):
        ratelist.write(''+str(scrubbed_data[i])+"    '"+str(scrubbed_data[i])+".txt'   \n")
    ratelist.close()
              
    print "Number of reactions in list not found:",len(failed_rates)

    return
    
    
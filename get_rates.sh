#!/bin/bash
awk '{print $2,$3}' reactions_list.txt > 'rate_list_w_q_values.txt'

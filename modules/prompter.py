########################################
#         IMPORT DEPENDENCIES          #
########################################
import pandas as pd
from pandasai import SmartDataframe
from pandasai import SmartDatalake
from pandasai.llm import OpenAI

from pandasai import Agent


########################################
#                                      #
########################################
#temukan model best approach / version of each process/module 
#kolom lebih dari 1 kalimat? ambil data dari dictionary?  

#dapetin table name (hasil proses lokker)
#ambil prompt, tau tujuannya apa
#let llm learn and generate the query
#output; one line of the retrieval pandas process / without import or print
########################################
# Intellectual property of Data Science - DMA - BNI. It is intended for use by authorized personnel only (Mentari ER, Atwin P, and Randu H)
# Unauthorized distribution, reproduction, or modification of this code, in whole or in part, is strictly prohibited
# without the express written consent of Data Science - DMA - BNI. Any use of this code outside the scope of its intended
# purpose must be authorized by Data Science - DMA - BNI. This code is provided "as is" without any warranty of any kind,
# express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose,
# and non-infringement. Data Science - DMA - BNI and the authors of this code shall not be liable for any damages, including
# but not limited to direct, indirect, special, incidental, or consequential damages or loss of profit, arising out of
# the use, inability to use, or performance of this code, even if Data Science - DMA - BNI or the authors have been advised
# of the possibility of such damages. By using this code, you agree to these terms and conditions.
########################################


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
# dapetin df query dari step promter
# run it, how to run it sampai dapat hasilnya
# output: angka atau tabel(dataframe)
from util.Pdf import PDF
import pandas as pd
from datetime import date

def gen_sample():
    
    df = pd.read_csv('testing/student.csv')

    txt = '''A report is written for a clear purpose and to a particular audience. Specific information and evidence are presented, analysed and applied to a particular problem or issue. The information is presented in a clearly structured format making use of sections and headings so that the information is easy to locate and follow.'''

    pdf = PDF('asset/logo.png')
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    pdf.cell(10, 10, str(date.today()),0,1)
    pdf.multi_cell(190, 8, txt)
    pdf.ln(10)
    pdf.cell(10,10,"Student data:",0,1)
    pdf.print_df(df=df, font_size=8)
    pdf.output('tmp/test_pdf.pdf','F')
    
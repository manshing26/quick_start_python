from typing import Union
from fpdf import FPDF
from pandas import DataFrame

class PDF(FPDF):
    def __init__(
        self,
        logo_path: Union[str,None] = None
        ):
        super().__init__()
        # A4 size = 210mm * 297mm
        self.WIDTH = 210
        self.HEIGHT = 297
        self.MARGIN = 10
        self.logo_path = logo_path
        
        
    def header(self):
        
        if self.logo_path != None:
            self.image(self.logo_path, 5, 5, 33)
            
        self.set_font('Arial', 'B', 11)
        self.cell(self.WIDTH - 80)
        self.cell(60, 1, 'Monthly Report', 0, 0, 'R')
        self.ln(10)
        self.cell(self.WIDTH - self.MARGIN*2, 0 ,border=1)
        self.ln(10)
        
    def footer(self):
        # Page numbers in the footer
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
    
    def print_df(self, df: DataFrame, font_size: int = 12):
        # table header
        self.set_font('Arial', 'B', font_size)
        
        columns = df.columns.to_list()
        df_length = len(df)
        for i in columns:
            if i != columns[-1]:
                self.cell(30, font_size, i.capitalize(), 1, 0, align='C')
            else:
                self.cell(30, font_size, i.capitalize(), 1, 1, align='C')
                
        # table content
        for i in range(df_length):
            for j in columns:
                text = str(df[j].iloc[i])
                if j != columns[-1]:
                    self.cell(30, font_size, text, 1, 0, align='C')
                else:
                    self.cell(30, font_size, text, 1, 1, align='C')
        
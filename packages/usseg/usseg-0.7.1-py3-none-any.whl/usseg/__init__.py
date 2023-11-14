"""Initialises the ultrasound-segmenetation module"""
from usseg import General_functions
from usseg.Organise_files import get_likely_us
from usseg.Single_image_processing import data_from_image
from usseg.Refined_anon_2_html import setup_tesseract, segment
from usseg.visualisation_html import generate_html_from_pkl, generate_html
from usseg.main import main
import os
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'

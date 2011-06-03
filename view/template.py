import os
from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions
import config


template_desktop = TemplateLookup(directories		=[ os.path.join(os.path.dirname(__file__),'template',config.template_desktop_path),
							   os.path.join(os.path.dirname(__file__),'template','portion')
							 ],
				  module_directory	= os.path.join(os.path.dirname(__file__),'..','tmp'),
				  output_encoding       ='utf-8', 
				  encoding_errors	='replace',
				  input_encoding	='utf-8'
				 );

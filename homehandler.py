
#
# main handler for the home page of chiibo.
#


# import statements
import sys
import os
sys.path.append(os.path.abspath('languages'))
import webapp2
import jinja2
import meta
import content_text
from google.appengine.api import mail
import datetime


# global properties
CHB_LANGUAGE = 'chb_language'


# configure Jinja2 template engine
template_dir = os.path.join(os.path.dirname(__file__), 'website')
jinja = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = False)


# configure meta translation engine
meta.set_directory('languages/')
_ = meta.translate


# handles all request to the home page
class HomeHandler(webapp2.RequestHandler):
	
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
		
	
    def render(self, template, **kw):
        self.write(jinja.get_template(template).render(kw))
        
         
    def get_language(self):
        language = self.request.get('lang')
        if language == '': language = self.request.cookies.get(CHB_LANGUAGE)
        
        if language == None:
            if 'Accept-Language' in self.request.headers:
                language_header = self.request.headers['Accept-Language']
                language = language_header.split('-')[0].split(',')[0]
            if language == None: language = 'us'
            
        return language
        
    
    def post(self):
        user_name = self.request.get('user_name')
        user_email = self.request.get('user_email')
        user_message = self.request.get('user_message')
        user_hello = self.request.get('user_hello')
        
        email_subject = 'Chiibo Website Form: ' + user_name + ' - ' + user_email
        
        contact_state = 'show-success'
        if not mail.is_email_valid(user_email):
            contact_state = 'show-error'
        else:
            if user_hello == 'chiibo hello world': mail.send_mail('admin@chiibo.com', 'hello@chiibo.com', email_subject, user_message)
        
        language = self.get_language()
        language = meta.set_language(language).encode('utf-8')
        expires = (datetime.datetime.now() + datetime.timedelta(weeks=56)).strftime('%a, %d %b %Y %H:%M:%S GMT')
        self.response.headers.add_header('Set-Cookie', '%s=%s; Path=/; Expires=%s' % (CHB_LANGUAGE, language, expires))
        self.render('home.html', chb_language = language,
        chb_description = _(content_text.chb_description),
        chb_ie_error = _(content_text.chb_ie_error),
        chb_contact_title = _(content_text.chb_contact_title),
        chb_contact_description = _(content_text.chb_contact_description),
        chb_contact_message_input = _(content_text.chb_contact_message_input),
        chb_contact_name_input = _(content_text.chb_contact_name_input),
        chb_contact_email_input = _(content_text.chb_contact_email_input),
        chb_contact_send_btn = _(content_text.chb_contact_send_btn),
        chb_contact_error_fields = _(content_text.chb_contact_error_fields),
        chb_contact_error_email = _(content_text.chb_contact_error_email),
        chb_contact_success = _(content_text.chb_contact_success),
        chb_navbar_specialties = _(content_text.chb_navbar_specialties),
        chb_navbar_process = _(content_text.chb_navbar_process),
        chb_navbar_team = _(content_text.chb_navbar_team),
        chb_navbar_footer = _(content_text.chb_navbar_footer),
        chb_topbar_contact_btn_closed = _(content_text.chb_topbar_contact_btn_closed),
        chb_topbar_contact_btn_opened = _(content_text.chb_topbar_contact_btn_opened),
        chb_topbar_contact_state = contact_state,
        chb_topbar_contact_btn = _(content_text.chb_topbar_contact_btn_closed),
        chb_topbar_backtop_btn = _(content_text.chb_topbar_backtop_btn),
        chb_intro_tagline = _(content_text.chb_intro_tagline),
        chb_intro_description = _(content_text.chb_intro_description),
        chb_intro_image_src = _(content_text.chb_intro_image_src),
        chb_specialties_title = _(content_text.chb_specialties_title),
        chb_specialties_tagline_one = _(content_text.chb_specialties_tagline_one),
        chb_specialties_tagline_two = _(content_text.chb_specialties_tagline_two),
        chb_specialties_tagline_three = _(content_text.chb_specialties_tagline_three),
        chb_specialties_description = _(content_text.chb_specialties_description),
        chb_specialties_web_title = _(content_text.chb_specialties_web_title),
        chb_specialties_web_description = _(content_text.chb_specialties_web_description),
        chb_specialties_apps_title = _(content_text.chb_specialties_apps_title),
        chb_specialties_apps_description = _(content_text.chb_specialties_apps_description),
        chb_specialties_design_title = _(content_text.chb_specialties_design_title),
        chb_specialties_design_description = _(content_text.chb_specialties_design_description),
        chb_specialties_deployment_title = _(content_text.chb_specialties_deployment_title),
        chb_specialties_deployment_description = _(content_text.chb_specialties_deployment_description),
        chb_specialties_prototype_title = _(content_text.chb_specialties_prototype_title),
        chb_specialties_prototype_description = _(content_text.chb_specialties_prototype_description),
        chb_specialties_revamp_title = _(content_text.chb_specialties_revamp_title),
        chb_specialties_revamp_description = _(content_text.chb_specialties_revamp_description),
        chb_process_title = _(content_text.chb_process_title),
        chb_process_tagline = _(content_text.chb_process_tagline),
        chb_process_description = _(content_text.chb_process_description),
        chb_process_step_1_title = _(content_text.chb_process_step_1_title),
        chb_process_step_1 = _(content_text.chb_process_step_1),
        chb_process_step_2_title = _(content_text.chb_process_step_2_title),
        chb_process_step_2 = _(content_text.chb_process_step_2),
        chb_process_step_3_title = _(content_text.chb_process_step_3_title),
        chb_process_step_3 = _(content_text.chb_process_step_3),
        chb_process_step_4_title = _(content_text.chb_process_step_4_title),
        chb_process_step_4 = _(content_text.chb_process_step_4),
        chb_team_title = _(content_text.chb_team_title),
        chb_team_tagline = _(content_text.chb_team_tagline),
        chb_team_description = _(content_text.chb_team_description),
        chb_team_devin = _(content_text.chb_team_devin),
        chb_team_enma = _(content_text.chb_team_enma),
        chb_team_enrique = _(content_text.chb_team_enrique),
        chb_footer_title = _(content_text.chb_footer_title),
        chb_footer_email_us = _(content_text.chb_footer_email_us),
        chb_footer_pick_language = _(content_text.chb_footer_pick_language),
        chb_footer_language_link = _(content_text.chb_footer_language_link),
        chb_footer_language_list = _(content_text.chb_footer_language_list),
        chb_footer_follow_our_feed = _(content_text.chb_footer_follow_our_feed))
        
    

    def get(self):
        language = self.get_language()
        language = meta.set_language(language).encode('utf-8')
        expires = (datetime.datetime.now() + datetime.timedelta(weeks=56)).strftime('%a, %d %b %Y %H:%M:%S GMT')
        self.response.headers.add_header('Set-Cookie', '%s=%s; Path=/; Expires=%s' % (CHB_LANGUAGE, language, expires))
        self.render('home.html', chb_language = language,
        chb_description = _(content_text.chb_description),
        chb_ie_error = _(content_text.chb_ie_error),
        chb_contact_title = _(content_text.chb_contact_title),
        chb_contact_description = _(content_text.chb_contact_description),
        chb_contact_message_input = _(content_text.chb_contact_message_input),
        chb_contact_name_input = _(content_text.chb_contact_name_input),
        chb_contact_email_input = _(content_text.chb_contact_email_input),
        chb_contact_send_btn = _(content_text.chb_contact_send_btn),
        chb_contact_error_fields = _(content_text.chb_contact_error_fields),
        chb_contact_error_email = _(content_text.chb_contact_error_email),
        chb_contact_success = _(content_text.chb_contact_success),
        chb_navbar_specialties = _(content_text.chb_navbar_specialties),
        chb_navbar_process = _(content_text.chb_navbar_process),
        chb_navbar_team = _(content_text.chb_navbar_team),
        chb_navbar_footer = _(content_text.chb_navbar_footer),
        chb_topbar_contact_btn_closed = _(content_text.chb_topbar_contact_btn_closed),
        chb_topbar_contact_btn_opened = _(content_text.chb_topbar_contact_btn_opened),
        chb_topbar_contact_state = _(content_text.chb_topbar_contact_state),
        chb_topbar_contact_btn = _(content_text.chb_topbar_contact_btn_closed),
        chb_topbar_backtop_btn = _(content_text.chb_topbar_backtop_btn),
        chb_intro_tagline = _(content_text.chb_intro_tagline),
        chb_intro_description = _(content_text.chb_intro_description),
        chb_intro_image_src = _(content_text.chb_intro_image_src),
        chb_specialties_title = _(content_text.chb_specialties_title),
        chb_specialties_tagline_one = _(content_text.chb_specialties_tagline_one),
        chb_specialties_tagline_two = _(content_text.chb_specialties_tagline_two),
        chb_specialties_tagline_three = _(content_text.chb_specialties_tagline_three),
        chb_specialties_description = _(content_text.chb_specialties_description),
        chb_specialties_web_title = _(content_text.chb_specialties_web_title),
        chb_specialties_web_description = _(content_text.chb_specialties_web_description),
        chb_specialties_apps_title = _(content_text.chb_specialties_apps_title),
        chb_specialties_apps_description = _(content_text.chb_specialties_apps_description),
        chb_specialties_design_title = _(content_text.chb_specialties_design_title),
        chb_specialties_design_description = _(content_text.chb_specialties_design_description),
        chb_specialties_deployment_title = _(content_text.chb_specialties_deployment_title),
        chb_specialties_deployment_description = _(content_text.chb_specialties_deployment_description),
        chb_specialties_prototype_title = _(content_text.chb_specialties_prototype_title),
        chb_specialties_prototype_description = _(content_text.chb_specialties_prototype_description),
        chb_specialties_revamp_title = _(content_text.chb_specialties_revamp_title),
        chb_specialties_revamp_description = _(content_text.chb_specialties_revamp_description),
        chb_process_title = _(content_text.chb_process_title),
        chb_process_tagline = _(content_text.chb_process_tagline),
        chb_process_description = _(content_text.chb_process_description),
        chb_process_step_1_title = _(content_text.chb_process_step_1_title),
        chb_process_step_1 = _(content_text.chb_process_step_1),
        chb_process_step_2_title = _(content_text.chb_process_step_2_title),
        chb_process_step_2 = _(content_text.chb_process_step_2),
        chb_process_step_3_title = _(content_text.chb_process_step_3_title),
        chb_process_step_3 = _(content_text.chb_process_step_3),
        chb_process_step_4_title = _(content_text.chb_process_step_4_title),
        chb_process_step_4 = _(content_text.chb_process_step_4),
        chb_team_title = _(content_text.chb_team_title),
        chb_team_tagline = _(content_text.chb_team_tagline),
        chb_team_description = _(content_text.chb_team_description),
        chb_team_devin = _(content_text.chb_team_devin),
        chb_team_enma = _(content_text.chb_team_enma),
        chb_team_enrique = _(content_text.chb_team_enrique),
        chb_footer_title = _(content_text.chb_footer_title),
        chb_footer_email_us = _(content_text.chb_footer_email_us),
        chb_footer_pick_language = _(content_text.chb_footer_pick_language),
        chb_footer_language_link = _(content_text.chb_footer_language_link),
        chb_footer_language_list = _(content_text.chb_footer_language_list),
        chb_footer_follow_our_feed = _(content_text.chb_footer_follow_our_feed))
		



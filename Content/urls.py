from os import name
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('',views.Content,name='content'),
    
    #path('login',views.login1,name='login'),
    #path('Forget_password',views.frgt_pswd,name='frgt_pswd'),
    #path('Forget_password_reset',views.frgt_pswd_msg,name='frgt_pswd_msg'),
    #path('Register',views.register,name='register'),
    
    #path('Signup',views.handleSignup,name='signup'),
    
    #path('Signout',views.handlesignout,name='signout'),
    #path('Delete',views.del_user,name='delete_user'),
    path('Check/',include('Check.urls'),name='check'),
    #PARTS OF SPEECH
    path('Nouns',views.nouns,name='nouns'),
    path('Pronouns',views.pronouns,name='pronouns'),
    path('Verbs',views.verbs,name='verbs'),
    path('Adverbs',views.adverbs,name='adverbs'),
    path('Adjectives',views.adjectives,name='adjectives'),
    path('Preposition',views.prepositions,name='prepositions'),
    path('Conjunctions',views.conjunctions,name='conjunctions'),
    path('Interjections',views.interjections,name='interjections'),
    
    #ARTICLES
    path('Articles',views.articles,name='articles'),

    #FILE
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
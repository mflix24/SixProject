import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Creating a function for calling LLAma2 model through  CTransformers() class
def getLLamaresponse(input_text,no_words,blog_style):
    ### creating an object of CTransformers() class
    llm=CTransformers(
        model='TheBloke/Llama-2-7B-Chat-GGML',
        model_type='llama',
        config={
            'max_new_tokens':256,
            'temperature':0.01
            })
    
    ## template creating for the systm
    template="""
        Write a blog for {blog_style} job profile
        for a topic {input_text}
        within {no_words} words.
        """
    # Calling PromptTemplate() class and making an object
    prompt=PromptTemplate(
        input_variables=["blog_style","input_text",'no_words'],
        template=template
        )
    
    # Generate the response from the object as llm through prompt.format() function
    response=llm(
        prompt.format(
            blog_style=blog_style,
            input_text=input_text,
            no_words=no_words
            ))
    return response

# Streamlit UI designing  by calling as set_page_config() function through streamlit as st
st.set_page_config(page_title="Generate Blogs",     # for the tile
                    page_icon='🤖',                 # for icon
                    layout='centered',              # for layout
                    initial_sidebar_state='collapsed')


# streamlit header
st.header("ChatBot For Generate Blogs 🤖")

# where user giving their input by text_input() function through streamlit
input_text=st.text_input("Enter the Blog Topic")


# creating two more columns for additonal 2 fields as no_words and blog_style
col1,col2=st.columns([5,5])
with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox(
        'Writing the blog for',
        ('Researchers','Data Scientist','Common People'),
        index=0
        )

# streamlit button caption='Generate'
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))






# st.set_page_config(page_title="Generate Blogs",
#                     page_icon='🤖',
#                     layout='centered',
#                     initial_sidebar_state='collapsed')

# st.header("Generate Blogs 🤖")

# input_text=st.text_input("Enter the Blog Topic")

# ## creating to more columns for additonal 2 fields

# col1,col2=st.columns([5,5])

# with col1:
#     no_words=st.text_input('No of Words')
# with col2:
#     blog_style=st.selectbox('Writing the blog for',
#                             ('Researchers','Data Scientist','Common People'),index=0)
    
# submit=st.button("Generate")

# ## Final response
# if submit:
#     st.write(getLLamaresponse(input_text,no_words,blog_style))
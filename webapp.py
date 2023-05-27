import streamlit as st
# import google.generativeai as palm
import os
import langchain
from langchain.chains import LLMChain
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

from langchain.llms import GooglePalm
from langchain.memory import ConversationBufferWindowMemory


# Configure the client library by providing your API key.
# palm.configure(api_key="AIzaSyBNQ-TmL3w1K54BwtjjoWPRaY-SHesJhxw")
os.environ["GOOGLE_API_KEY"] = "AIzaSyBNQ-TmL3w1K54BwtjjoWPRaY-SHesJhxw"

# Initialize LLM
llm = GooglePalm(temperature = 1.0,
  top_k = 40,
  top_p = 0.95,
  max_output_tokens = 5000,
  n =  1)

# Project Title
st.title(':blue[Solo]-:red[Preneur] :orange[Optimized] :blue[Content] :green[Kickstarter] (:blue[S].:red[P].:orange[O].:blue[C].:green[K]) 🖖')

image_path = "spock.png"

st.image(image_path, caption='Live Long & Prosper', width=300)
st.markdown("---")
st.markdown('## Select :blue[Cover Letter], :orange[Freelance Project Proposal], or :green[College App Essay]')
st.markdown('Choose whether you want to generate a cover letter for a Job application, generate a project proposal for Freelancing/bid-based work, or generate a college application essay.')
st.markdown("---")


# Display horizontal radio buttons
option = st.radio("Select an option", ("Cover Letter", "Project Proposal", "College App Essay"), index=0,horizontal=True)

# Conditionally display forms based on selected option
if option == "Cover Letter":
    # Display form for Option 1
    st.markdown("### Submit Form for :blue[Cover Letter]")
    col1, col2, col3 = st.columns(3)
    with col1:
        username = st.text_input("Your Name", placeholder ="Abish")

    with col2:
        company = st.text_input("Company Name (ex. Google)", placeholder ="Google")

    with col3:
        hiring_manager = st.text_input("Hiring Manager Name (Optional)", "None")
     
    job_details = st.text_area("Job Details",placeholder =  """(Copy and Paste from Linkedin Recommended)
    
    ie. 7 years of experience as a solution architect or technical consultant in a cloud computing environment or a customer or partner-facing role.
Experience with cloud computing (e.g., Artificial Intelligence/Machine Learning, Big Data, PaaS, and IaaS technologies).
Experience with machine learning frameworks.

Preferred qualifications:

Experience architecting production machine learning systems on distributed infrastructure.
Experience developing and deploying one or more applied AI/ML solutions in cloud environments.
Experience presenting and delivering technical presentations to large audiences.
Experience integrating databases into AI/ML solutions.
Experience architecting and deploying machine learning operations pipelines.
Ability to learn, understand, and work with new and emerging technologies, methodologies, and solutions in the Cloud/IT technology space.

About The Job

When leading companies choose Google Cloud it's a huge win for spreading the power of cloud computing globally. Once educational institutions, government agencies, and other businesses sign on to use Google Cloud products, you come in to facilitate making their work more productive, mobile, and collaborative. You listen and deliver what is most helpful for the customer. You assist fellow sales Googlers by problem-solving key technical issues for our customers. You liaise with the product marketing management and engineering teams to stay on top of industry trends and devise enhancements to Google Cloud products.

As a Partner Engineer, you will work with Partner Development Managers to grow and support the Google Cloud partner ecosystem in the Artificial Intelligence/Machine Learning (AI/ML) domain. You will understand the technical capabilities of our partners.

In this role, you will lead the effort to enable partners across technologies and solutions. You will contribute to customer adoption of Google Cloud by supporting partners, bringing the services to market faster, and create new business growth streams. You will help partners in the migration and deployment phase, ensuring they have access to Google Cloud artifacts, tools, templates, and best practices.

Google Cloud accelerates organizations’ ability to digitally transform their business with the best infrastructure, platform, industry solutions and expertise. We deliver enterprise-grade solutions that leverage Google’s cutting-edge technology – all on the cleanest cloud in the industry. Customers in more than 200 countries and territories turn to Google Cloud as their trusted partner to enable growth and solve their most critical business problems.

The US base salary range for this full-time position is $139,000-$213,000 + bonus + equity + benefits. Our salary ranges are determined by role, level, and location. The range displayed on each job posting reflects the minimum and maximum target for new hire salaries for the position across all US locations. Within the range, individual pay is determined by work location and additional factors, including job-related skills, experience, and relevant education or training. Your recruiter can share more about the specific salary range for your preferred location during the hiring process.

Please note that the compensation details listed in US role postings reflect the base salary only, and do not include bonus, equity, or benefits. Learn more about benefits at Google .

Responsibilities

Build partner specific, go-to-market solutions in AI/ML space to reduce business cycles and drive partner business as measured through business growth.
Recommend integration and migration strategies, enterprise architectures, platforms, and application infrastructure required to implement a complete solution on Google Cloud.
Own the technical relationship with our partners, empowering them to drive a pilot or proof of concept on the latest AI/ML offerings.
Work with partners during the implementation phase to assure they have all the tools necessary to deliver a successful deployment.
Support partners towards customer acceptance of the technical proposal, leading to a commercial proposal, and eventual agreement.""")
    additional_details = st.text_area("Personal Skills Highlights", placeholder = """(Any and everything additional you would like to include about your personal skills, does not have to be complete sentences)
    for example:
    I have a Masters degree in computational medicine""")

    
    submit_button1 = st.button("Submit Form for Cover Letter")
    if submit_button1:
        st.markdown("##### Wait a minute content is generating...")
        st.markdown("---")
        if hiring_manager == 'None' or hiring_manager == '':
            hiring_manager = 'Employer'
        
        # Cover Letter Writer
        template =f"Assistant is designed to create a cover letter to company {company} with hiring manager named {hiring_manager} based on job details provided by the user named {username}. Assistant will highlight the additional details section provided by the user in the generated cover letter. Job Details: {job_details} Additional Details: {additional_details}"
        prompt = PromptTemplate(
            input_variables=[], 
            template=template
        )
        chatgpt_chain = LLMChain(
    llm=llm, 
    prompt=prompt, 
    verbose=True, 
    memory=ConversationBufferWindowMemory(k=1),
)
        output = chatgpt_chain.predict( text="Generate a cover letter")
        st.markdown(output)
        st.markdown("---")
 

                
if option == "Project Proposal":
    # Display form for Option 2
    st.markdown("### Submit Form for :orange[Project Proposal]")
    col1, col2 = st.columns(2)
    with col1:
        username = st.text_input("Your Name", placeholder ="Abish")

    with col2:
        desired_salary = st.number_input("Expected Hourly Salary", value = 50)

    job_details = st.text_area("Job Details",placeholder =  """(Copy and Paste from Freelance site Recommended)
    We are SEO consultants looking to track the ecommerce revenue that our pages generate for a client. We need someone to set up reporting in BigQuery for a group of pages that tracks everyone who views these pages and then purchases from the site within 30 days. The site will have Google Tag Manager set up.

We need instructions for how to tag pages that we create, and then for you to set up reporting. The goal of reporting is to show revenue for the pages as a group, and then revenue and conversion rate broken down by page as well, and be able to adjust the time period. Ideally, would also like to have a report of individual purchasers so that busienss owner could match back into his platform. Also, would only want to track organic visitors.

If this is something you can do, please reply with relevant examples of prior work, and a quote for the project cost.""")
    
    additional_details = st.text_area("Personal Skills Highlights", placeholder = """(Any and everything additional you would like to include about your personal skills, does not have to be complete sentences)
    for example:
    I have a Masters degree in computational medicine""")
    
   
    submit_button2 = st.button("Submit Form for Project Proposal")
    if submit_button2:
        st.markdown("##### Wait a minute content is generating...")
        st.markdown("---")
        # Soloprenuer
        template =f"Assistant is designed to create a job proposal for a freelancing job with an estimate on the hours it will take as well as a price quote from an hourly salary of {desired_salary}. Always start job proposal with 'Dear Employer'. Assisstant will highlight additional skills provided by the user named {username}. Freelancing Job Details: {job_details} Additional Details: {additional_details}"

        prompt = PromptTemplate(
            input_variables=[], 
            template=template
        )
        chatgpt_chain = LLMChain(
    llm=llm, 
    prompt=prompt, 
    verbose=True, 
    memory=ConversationBufferWindowMemory(k=1),
)
        output = chatgpt_chain.predict( text="Generate the proposal")
        st.markdown(output)
        st.markdown("---")

        

if option == "College App Essay":
    # Display form for Option 2
    st.markdown("### Submit Form for :green[College App Essay]")
    word_limit = st.number_input("Word Limit", value = 250, step = 50)
    essay = st.text_area("Essay Question", placeholder= "Copy and Paste in the Essay Question")
    
    additional_details = st.text_area("Skills Highlight", placeholder = """(Any and everything additional you would like to include in your essay, does not have to be complete sentences)
    for example:
    I am interested in its pre-medicine program""")
    
    submit_button3 = st.button("Submit Form for College App Essay")
    if submit_button3:
        st.markdown("##### Wait a minute content is generating...")
        st.markdown("---")
        # college essay
        template =f"Assistant is designed to write college application essays in {word_limit} words. Begin Essay Question: {essay} [End Essay] \n"

        if additional_details != '':
            template += f"In the essay response highlight these additional skills or interestes: {additional_details} "

        prompt = PromptTemplate(
            input_variables=[], 
            template=template
        )
        
        chatgpt_chain = LLMChain(
    llm=llm, 
    prompt=prompt, 
    verbose=True, 
    memory=ConversationBufferWindowMemory(k=1),
)

        output = chatgpt_chain.predict( text=f"Write the essay in {word_limit} words")
        st.markdown(output)
        
        st.markdown("---")
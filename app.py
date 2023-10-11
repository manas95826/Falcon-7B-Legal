import streamlit as st
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub
import os

os.environ['OPENAI_API_KEY'] = ''
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'
# Import your model and template
llm_hf = HuggingFaceHub(
    repo_id="tiiuae/falcon-7b-instruct",
    model_kwargs={"temperature": 0.3}
)

restaurant_template = """
I want you to become an indian lawyer and enlist me the acts and rights with a one liner description, for every issue i'll raise, you've to only give me relevant acts and rights coving from that issue for example:
The Indian Contract Act, 1872: This act governs the basic principles of contract law, which includes rent agreements. It sets the legal framework for agreements and their enforceability.

The Rent Control Act (varies by state): Different Indian states have their own Rent Control Acts that regulate rent agreements, rent control, and tenant-landlord relationships. You should consult the specific Rent Control Act relevant to your location for details.

Right to Property: As per the Indian Constitution, the right to property is a fundamental right, but it's not absolute. You have the right to enjoy your property and enter into agreements, including rent agreements, as long as it is in compliance with the law.

Tenant's Rights: Tenants in India also have rights, such as the right to peaceful enjoyment of the rented premises, right to a fair and reasonable rent, and right to notice for eviction. These rights may vary by state. 
etc.
you've to answer me like this for every issue i'll raise, 
here's the example issue:
{issue}
"""

# Define the Streamlit app
def main():
    st.title("Indian Legal Consultation")
    
    # Input for the user's issue
    description = st.text_area("Please describe your issue:")

    if st.button("Get Legal Advice"):
        if description:
            # Create a PromptTemplate
            prompt = PromptTemplate(
                input_variables=["issue"],
                template=restaurant_template,
            )
            
            # Create an LLMChain
            chain = LLMChain(llm=llm_hf, prompt=prompt)
            
            # Generate a response
            response = chain.run(description)
            
            # Display the response
            st.subheader("Legal Advice:")
            st.write(response)
        else:
            st.warning("Please provide a description of your issue.")

if __name__ == "__main__":
    main()

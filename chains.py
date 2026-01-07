from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain_openai import ChatOpenAI

from schema import InvoiceInfo


def create_extraction_prompt() -> ChatPromptTemplate:
    """
    This Function :
        1. Creates PydanticOutputParser
        2. Creates SystemMessage defining the AI role
        3. Creates HumanMessage that includes place holders for invoice text and format instructions for output
        4. Returns a ChatPromptTempalte object with partial prefil of format instructions

    Input: None

    Output: ChatPromptTemplate -> A prompt ready for use with only Invoice Text to be provided when running

    """
    parser = PydanticOutputParser(pydantic_object=InvoiceInfo)
    format_instructions = parser.get_format_instructions()
    system_message = SystemMessagePromptTemplate.from_template(
        template="""You are expert document processor. Your task is to extract structured infromation from invoices accurately."""
    )
    human_message = HumanMessagePromptTemplate.from_template(
        template=""" Here is the raw invoice text: \n\n{invoice_text}\n\n
    Please extract invoice details and format them exactly according to these instructions:\n{format_instructions}."""
    )
    return (
        ChatPromptTemplate.from_messages([system_message, human_message]).partial(
            format_instructions=format_instructions
        ),
        parser,
    )


def get_extraction_chain():
    prompt, parser = create_extraction_prompt()
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)
    chain = prompt | llm | parser
    return chain

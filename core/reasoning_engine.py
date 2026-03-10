def reason(question, context):

    analysis = f"Analyzing: {question}"

    if context:
        analysis += " using external data"

    return analysis

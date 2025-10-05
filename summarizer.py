from transformers import pipeline  # Import the AI toolbox

def summarize_text(text, max_sentences=3):
    """
    This function summarizes the input text into up to 3 sentences using AI.
    
    Args:
        text (str): The long article or blog post you want to summarize.
        max_sentences (int): Max number of sentences (default: 3).
    
    Returns:
        str: The short summary.
    """
    # Load the AI model (downloads first time, then fast)
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    # Run the AI: Limit summary length to fit 3 sentences
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    
    # Get the summary text
    summarized = summary[0]['summary_text']
    
    # Split into sentences and limit to 3 (if longer)
    sentences = summarized.split('. ')
    if len(sentences) > max_sentences:
        summarized = '. '.join(sentences[:max_sentences]) + '.'
    
    return summarized

if __name__ == "__main__":
    # Example: Paste your own article text here (replace the sample below)
    article_text = """
    Climate change is one of the most pressing issues of our time. Rising global temperatures are leading to more frequent extreme weather events, such as hurricanes, droughts, and wildfires. Scientists warn that if emissions continue unchecked, we could see sea levels rise by several feet by 2100, displacing millions. Governments worldwide are pushing for renewable energy transitions, but challenges like political resistance and economic costs remain. Individuals can help by reducing waste and supporting green policies. Recent reports show that 2023 was the hottest year on record, with glaciers melting faster than ever.
    """
    
    print("Original Text:")
    print(article_text)
    print("\nSummary (3 sentences):")
    summary = summarize_text(article_text)
    print(summary)
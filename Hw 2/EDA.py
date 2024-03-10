### EDA


# Perform EDA on the dataset
import matplotlib.pyplot as plt
plt.rc('font', size=14)
import seaborn as sns
sns.set(style='white')
sns.set(style='whitegrid', color_codes=True)
import pandas as pd
from wordcloud import WordCloud

import warnings
warnings.filterwarnings('ignore')

def Get_numeric_visualize(df, x, y='loan_status'):
    """
    Get density for specific variable x respect to default group and non-default group

    Input:
    x  : variable to concern
    y  : Label, loan_status here
    df : DataFrame, loan_data here

    Output:
    The density plot for specific variable x respect to default group and non-default group
    """
    
    # Filter the DataFrame for default and non-default groups based on loan_status
    default_group = df[df[y] == 'Charged Off'][x]
    non_default_group = df[df[y] != 'Charged Off'][x]
    
    sns.kdeplot(default_group, label='Default', color="blue",fill=True)
    sns.kdeplot(non_default_group, label='Non-Default', color="red", fill = True)

    plt.xlabel(x)
    plt.ylabel('Density')
    plt.title('Density Plot of ' + x + ' by Loan Status')
    
    plt.legend()
    plt.show()
    
    ##############################################################################
    #                               END OF YOUR CODE                             #
    ##############################################################################

def Get_category_visualize(df,x,y = 'loan_status'):
    '''
       Get count plot for specific variable x respect to default group and non-default group

       Input:
       x     : variable to concern
       y     : Label, loan_status here
       df    : DataFrame, loan_data here

       Output:
       The count plot for specific variable x respect to default group and non-default group
       '''
    ##############################################################################
    ### TODO: Get count bar plot for specific variable x                       ###
    ### HINT: Consider using sns.countplot() method                            ###
    ##############################################################################
    # Set the figure size for better readability
    plt.figure(figsize=(10, 6))
    
    # Create the count plot
    sns.countplot(data=df, x=x, hue=y)
    
    # Set the title and labels
    plt.title(f'Count Plot of {x} by {y}')
    plt.xlabel(x)
    plt.ylabel('Count')
    
    # Display the plot
    plt.show()
        
    ##############################################################################
    #                               END OF YOUR CODE                             #
    ##############################################################################

def Get_text_visualize(df,x,y = 'loan_status'):
    '''
       Using wordcloud to visualize text data

       Input:
       x     : variable to concern
       y     : Label, loan_status here
       df    : DataFrame, loan_data here

       Output:
       The wordcloud plot for specific variable x respect to default group
       '''
    ##############################################################################
    ### TODO: Get wordcloud for specific variable x(text data)                 ###
    ### HINT: Consider using wordcload module                                  ###
    ##############################################################################
    df = df[df[x].notnull()]
    default_text = " ".join([str(text) for text in df[df[y] == 'Charged Off'][x]])
    default_wordcloud = WordCloud(background_color="white").generate(default_text)
    
    # Display the word cloud using matplotlib
    plt.figure(figsize=(10, 6))
    plt.imshow(default_wordcloud, interpolation='bilinear')
    plt.axis('off')  # Remove the axis
    plt.title(f'Word Cloud for {x} in Default Group')
    plt.show()

    ##############################################################################
    #                               END OF YOUR CODE                             #
    ##############################################################################


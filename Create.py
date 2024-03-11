import sqlite3

# Function to create tables
def create_tables(conn):
    categories = [
        'Strategic_Management',
        'Digital_Marketing',
        'Personal_Sales',
        'Information_Systems',
        'Project_Management'
    ]

    for category in categories:
        query = f'''
        CREATE TABLE IF NOT EXISTS {category} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        );
        '''
        conn.execute(query)

# Function to add data to tables
def add_data(conn, category, questions):
    query = f'INSERT INTO {category} (question, answer) VALUES (?, ?);'
    conn.executemany(query, questions)

# Main function to create tables and add data
def main():
    # Connect to the database
    conn = sqlite3.connect('quiz_bowl.db')

    # Create tables
    create_tables(conn)

    # Sample questions for each category (replace with actual questions)
    strategic_management_questions = [
        ('What is SWOT analysis?', 'Strengths, Weaknesses, Opportunities, Threats'),
        ('Define competitive advantage.', 'A unique advantage that allows a business to outperform its rivals'),
        ("Define core competencies in the context of strategic management.", "Distinctive capabilities that provide a competitive advantage"),
        ("What is the purpose of a PESTLE analysis?", "To identify and analyze external factors affecting an organization"),
        ("Explain the concept of diversification in business strategy.", "Expanding into new markets or products to reduce risk"),
        ("What role does the SWOT analysis play in strategic planning?", "Identifying internal strengths and weaknesses, and external opportunities and threats"),
        ("Define the term 'strategic vision' in strategic management.", "A clear and inspiring long-term direction for the organization"),
        ("How does the BCG matrix categorize products?", "Into stars, cash cows, question marks, and dogs based on market share and growth rate"),
        ("What is the difference between differentiation and cost leadership strategies?", "Differentiation focuses on uniqueness, while cost leadership aims for the lowest cost in the industry"),
        ("Explain the significance of a mission statement in strategic management.", "Communicates the purpose and values of an organization to stakeholders")
        # Add more questions here...
    ]

    digital_marketing_questions = [
        ('What is SEO?', 'Search Engine Optimization'),
        ('Explain the concept of conversion rate optimization (CRO).', 'Improving the percentage of website visitors who take a desired action'),
        ("Explain the concept of inbound marketing.", "Attracting customers through valuable content and experiences"),
        ("What is the purpose of A/B testing in digital marketing?", "To compare two versions of a webpage or campaign to determine which performs better"),
        ("Define the term 'conversion rate' in online marketing.", "The percentage of website visitors who complete a desired goal"),
        ("How does social media marketing contribute to brand awareness?", "By engaging with a target audience and sharing relevant content"),
        ("What is the role of a call-to-action (CTA) in email marketing?", "Encourages recipients to take a specific action, such as clicking a link or making a purchase"),
        ("Explain the concept of retargeting in digital advertising.", "Displaying ads to users who have previously visited a website or interacted with certain content"),
        ("Define the term 'keyword research' in the context of SEO.", "The process of identifying relevant search terms to optimize content and improve search engine rankings"),
        ("How does pay-per-click (PPC) advertising work?", "Advertisers pay a fee each time their ad is clicked, driving traffic to their website")
        # Add more questions here...
    ]

    personal_sales_questions = [
        ('What is consultative selling?', 'A sales approach focused on building relationships and understanding customer needs'),
        ('Define objection handling in sales.', 'Addressing and overcoming customer concerns or objections'),
        ("Explain the concept of relationship selling in personal sales.", "Building and maintaining strong relationships with customers to drive long-term success"),
        ("What role does active listening play in effective sales communication?", "Understanding customer needs and concerns through careful attention and response"),
        ("Define the term 'sales objection' and provide an example.", "Customer concerns or hesitations, e.g., objections related to price, features, or competition"),
        ("How does the SPIN selling technique work?", "Situation, Problem, Implication, Need-payoff - a questioning technique to uncover customer needs and pain points"),
        ("What is the importance of product knowledge in sales?", "Enables sales professionals to effectively communicate the value and benefits of a product or service"),
        ("Explain the concept of upselling in personal sales.", "Encouraging customers to purchase a higher-end product or additional features"),
        ("Define the term 'closing' in the context of sales.", "The final step in the sales process, securing a commitment or agreement from the customer"),
        ("How can storytelling be used in sales presentations?", "Engaging customers by sharing relatable stories to highlight product benefits and solutions")
        # Add more questions here...
    ]

    information_systems_questions = [
        ('What is a database?', 'A structured collection of data'),
        ('Explain the difference between a router and a switch.', 'Router connects different networks, while a switch connects devices within a network'),
        # Add more questions here...
    ]

    project_management_questions = [
        ('What is the critical path in project management?', 'The longest sequence of tasks determining the project duration'),
        ('Define risk management in projects.', 'Identifying, assessing, and mitigating potential project risks'),
        # Add more questions here...
    ]

    # Add data to tables
    add_data(conn, 'Strategic_Management', strategic_management_questions)
    add_data(conn, 'Digital_Marketing', digital_marketing_questions)
    add_data(conn, 'Personal_Sales', personal_sales_questions)
    add_data(conn, 'Information_Systems', information_systems_questions)
    add_data(conn, 'Project_Management', project_management_questions)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()

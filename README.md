# Daily Expense Tracker

This is a web-based **Daily Expense Tracker** built using **Streamlit** that helps users record, analyze, and visualize their daily expenses. The application allows users to input their daily expenses, provides insights into their spending habits, and generates visual analysis based on the entered data.

## Features
- **Add Expense:** Users can log new expenses by entering the date, amount, and selecting a category (e.g., Grocery, Snacks, etc.).
- **View All Expenses:** The application displays all logged expenses in a structured DataFrame on the sidebar.
- **Summary Insights:** Provides key insights such as total expenses, highest spending category, and most expensive day.
- **Visual Analysis:** Displays a bar or line chart to visualize expenses over time based on the category.
- **AI-Powered Expense Queries:** Using Google's Gemini API and a Retrieval Augmented Generation (RAG) approach, users can ask questions about their expenses and receive intelligent responses.

## Technologies Used
- **Streamlit**: For building the web application interface.
- **Pandas**: To manage and manipulate expense data in tabular form.
- **Plotly**: For creating interactive visualizations of the expense data.
- **TF-IDF (Term Frequency-Inverse Document Frequency)**: For vectorizing the data and finding relevant expense entries using the RAG approach.
- **Google Gemini API**: For generating intelligent responses based on expense data.
- **Sklearn (scikit-learn)**: For implementing the cosine similarity metric used in retrieving relevant data chunks.

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.7+
- Required Python libraries:
  ```bash
  pip install streamlit pandas plotly scikit-learn requests
  ```	

### API Key Configuration
You'll need a Google Gemini API key to use the AI-powered query feature. You can set it up by replacing the API key directly in the `api_key` variable in the source code.

```python
api_key = "YOUR_GOOGLE_GEMINI_API_KEY"
```

## File Structure
```bash
├── app.py          # Main Streamlit application
├── requirements.txt
└── README.md            
```

## How to Run the Application

1. Clone this repository:
   ```bash
   git clone https://github.com/RAHULMYDUR/Advanced-Daily-Expense-Tracker-using-streamlt.git
   ```

2. Navigate to the project directory:
   ```bash
   cd daily-expense-tracker
   ```

3. Ensure you have all required dependencies installed:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. The application will open in your browser.

## Application Sections

### 1. Add New Expense
   - Users can input new expenses by selecting the date, entering the amount, and choosing the category (e.g., Grocery, Snacks, etc.).
   - Click the "Add Expense" button to record the expense.

### 2. View All Expenses (in Sidebar)
   - All recorded expenses are displayed in a structured DataFrame in the sidebar.
   - This allows users to easily track all their logged expenses.

### 3. Summary Insights
   - Total Expenses: Displays the total amount of money spent.
   - Highest Spending Category: Shows the category where the most money was spent.
   - Highest Spending Day: Displays the date with the highest spending.

### 4. Visual Analysis
   - Users can choose between a **Bar Chart** or a **Line Chart** to visualize their expenses over time, with color-coded categories.

### 5. AI-Powered Expense Query
   - Users can enter a natural language query related to their expenses (e.g., "What is my most expensive day?" or "How much did I spend on snacks?").
   - The AI will retrieve the most relevant entries from the expense data and generate a coherent answer using Google's Gemini API.

## Customization and Extension

1. **Adding New Categories**: 
   You can add more categories for expenses by modifying the `category` dropdown in the "Add New Expense" section:
   ```python
   category = st.selectbox("Category", ["Grocery", "Snacks", "Outside Eatings", "Others", "New Category"])
   ```

2. **Changing Visualizations**: 
   The application currently supports **Bar Chart** and **Line Chart** visualizations. You can extend this to include other chart types like **Pie Charts** by modifying the `plot_expense_data` function.

3. **Enhancing AI Querying**:
   The AI query feature uses a basic Retrieval Augmented Generation (RAG) approach. You can enhance this by training custom models or improving chunk retrieval with more advanced techniques.

## Future Enhancements

1. **Authentication**: Add user authentication to store and track expenses on a per-user basis.
2. **Expense Category Insights**: Provide more detailed insights per category, such as average spending or trends over time.
3. **Monthly and Yearly Views**: Extend the app to allow users to filter their expenses based on custom date ranges like monthly or yearly analysis.
4. **Expense Upload**: Allow users to upload CSV files to bulk import their past expenses.

## Troubleshooting

### Common Issues:
1. **CSV File Not Found**:
   - If the `daily_expenses.csv` file is missing, the application will automatically create a new one. However, ensure you have the necessary file permissions in the directory.

2. **Gemini API Not Working**:
   - Ensure that your API key is correct and has the necessary permissions.
   - Check that your internet connection is stable and that there are no firewall restrictions.

3. **Dependency Issues**:
   - If you face any errors related to missing Python packages, install the required libraries using:
     ```bash
     pip install -r requirements.txt
     ```

## Screenshots

### Add New Expense and Summary Insights
![2](https://github.com/user-attachments/assets/5c79ce1c-175c-4608-87ed-dc1b8f1650cd)

### Expense Visualization

### Chat interface

![1](https://github.com/user-attachments/assets/1013b88a-8b30-40a0-9455-968b3d050721)

## License
This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.



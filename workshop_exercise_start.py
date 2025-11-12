{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# PSUT Data Analysis Workshop - Hands-On Exercises\n",
    "## From Raw Data to Business Insights\n",
    "\n",
    "**Welcome!** In this notebook, you'll analyze real e-commerce data from a Jordanian online store.\n",
    "\n",
    "### Learning Objectives\n",
    "By the end of this exercise, you will be able to:\n",
    "- ✅ Load and explore datasets using Pandas\n",
    "- ✅ Perform data aggregation and grouping\n",
    "- ✅ Calculate descriptive statistics\n",
    "- ✅ Create meaningful visualizations\n",
    "- ✅ Answer business questions with data\n",
    "\n",
    "### Instructions\n",
    "- Read each cell carefully\n",
    "- Fill in the blanks marked with `# YOUR CODE HERE`\n",
    "- Run cells using `Shift + Enter`\n",
    "- Don't worry about making mistakes - that's how we learn!\n",
    "\n",
    "Let's begin! 🚀"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "## Part 1: Setup & Data Loading\n",
    "\n",
    "First, we need to import the libraries we'll use and load our data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import necessary libraries\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Set visualization style\n",
    "sns.set_style('whitegrid')\n",
    "plt.rcParams['figure.figsize'] = (10, 6)\n",
    "\n",
    "print(\"✅ Libraries imported successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load the dataset\n",
    "# The file is located in the 'data' folder one level up from this notebook\n",
    "df = pd.read_csv('../data/jordan_ecommerce_sample.csv')\n",
    "\n",
    "print(\"✅ Data loaded successfully!\")\n",
    "print(f\"\\nDataset shape: {df.shape[0]} rows, {df.shape[1]} columns\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "## Part 2: Data Exploration\n",
    "\n",
    "Before analyzing data, we always start by understanding what we're working with."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Display the first 5 rows\n",
    "print(\"First 5 rows of our dataset:\")\n",
    "print(\"=\"*80)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get information about the dataset\n",
    "print(\"Dataset Information:\")\n",
    "print(\"=\"*80)\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get statistical summary\n",
    "print(\"Statistical Summary:\")\n",
    "print(\"=\"*80)\n",
    "df.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 🤔 Quick Questions\n",
    "\n",
    "Based on what you see above:\n",
    "1. How many transactions do we have in total?\n",
    "2. What are the column names?\n",
    "3. What's the date range of our data?\n",
    "\n",
    "**Think about these - we'll discuss them!**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "## Part 3: Business Question #1\n",
    "### 🎯 Which city generates the most revenue?\n",
    "\n",
    "This is a common business question. Let's answer it step by step."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 1: Group by city and sum the total_amount\n",
    "revenue_by_city = df.groupby('city')['total_amount'].sum()\n",
    "\n",
    "# Step 2: Sort from highest to lowest\n",
    "revenue_by_city = revenue_by_city.sort_values(ascending=False)\n",
    "\n",
    "# Display results\n",
    "print(\"Revenue by City (JOD):\")\n",
    "print(\"=\"*50)\n",
    "print(revenue_by_city)\n",
    "print(\"\\n\" + \"=\"*50)\n",
    "print(f\"Top City: {revenue_by_city.index[0]} with {revenue_by_city.iloc[0]:.2f} JOD\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 📊 Visualize It!\n",
    "\n",
    "Numbers are good, but visualizations tell better stories."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a bar chart\n",
    "plt.figure(figsize=(12, 6))\n",
    "revenue_by_city.plot(kind='bar', color='steelblue', edgecolor='black')\n",
    "\n",
    "# Customize the chart\n",
    "plt.title('Total Revenue by City', fontsize=16, fontweight='bold', pad=20)\n",
    "plt.ylabel('Total Revenue (JOD)', fontsize=12)\n",
    "plt.xlabel('City', fontsize=12)\n",
    "plt.xticks(rotation=45, ha='right')\n",
    "plt.grid(axis='y', alpha=0.3)\n",
    "\n",
    "# Add value labels on top of bars\n",
    "for i, v in enumerate(revenue_by_city):\n",
    "    plt.text(i, v + 500, f'{v:,.0f}', ha='center', fontsize=10, fontweight='bold')\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()\n",
    "\n",
    "print(\"\\n💡 Insight: Amman clearly dominates the revenue!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "## Part 4: Business Question #2\n",
    "### 🎯 What's the average order value?\n",
    "\n",
    "Understanding typical order sizes helps with pricing and inventory strategies.\n",
    "\n",
    "**Now it's YOUR turn!** Fill in the blanks below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate average order value\n",
    "# Hint: Use the .mean() method on the 'total_amount' column\n",
    "\n",
    "average_order = # YOUR CODE HERE\n",
    "\n",
    "# Display the result\n",
    "print(f\"Average Order Value: {average_order:.2f} JOD\")\n",
    "\n",
    "# Bonus: Let's also calculate median and standard deviation\n",
    "median_order = df['total_amount'].median()\n",
    "std_order = df['total_amount'].std()\n",
    "\n",
    "print(f\"Median Order Value: {median_order:.2f} JOD\")\n",
    "print(f\"Standard Deviation: {std_order:.2f} JOD\")\n",
    "\n",
    "print(\"\\n💡 Why does median differ from mean? Think about outliers!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 📊 Distribution of Order Values\n",
    "\n",
    "Let's visualize the distribution to understand the pattern better."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a histogram\n",
    "plt.figure(figsize=(12, 6))\n",
    "plt.hist(df['total_amount'], bins=30, color='coral', edgecolor='black', alpha=0.7)\n",
    "\n",
    "# Add vertical lines for mean and median\n",
    "plt.axvline(average_order, color='red', linestyle='--', linewidth=2, label=f'Mean: {average_order:.2f} JOD')\n",
    "plt.axvline(median_order, color='green', linestyle='--', linewidth=2, label=f'Median: {median_order:.2f} JOD')\n",
    "\n",
    "plt.title('Distribution of Order Values', fontsize=16, fontweight='bold')\n",
    "plt.xlabel('Order Value (JOD)', fontsize=12)\n",
    "plt.ylabel('Frequency (Number of Orders)', fontsize=12)\n",
    "plt.legend(fontsize=10)\n",
    "plt.grid(axis='y', alpha=0.3)\n",
    "plt.tight_layout()\n",
    "plt.show()\n",
    "\n",
    "print(\"\\n💡 Most orders are between 50-200 JOD!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "## Part 5: Business Question #3\n",
    "### 🎯 Which product categories are most popular?\n",
    "\n",
    "Understanding what customers buy helps with inventory management.\n",
    "\n",
    "**Your turn again!**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Count how many orders each product category has\n",
    "# Hint: Use .value_counts() on the 'product_category' column\n",
    "\n",
    "top_products = # YOUR CODE HERE\n",
    "\n",
    "# Display top 5\n",
    "print(\"Top 5 Product Categories by Number of Orders:\")\n",
    "print(\"=\"*50)\n",
    "print(top_products.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visualize product popularity\n",
    "plt.figure(figsize=(12, 6))\n",
    "top_products.plot(kind='barh', color='lightgreen', edgecolor='black')\n",
    "\n",
    "plt.title('Product Category Popularity', fontsize=16, fontweight='bold', pad=20)\n",
    "plt.xlabel('Number of Orders', fontsize=12)\n",
    "plt.ylabel('Product Category', fontsize=12)\n",
    "plt.grid(axis='x', alpha=0.3)\n",
    "\n",
    "# Add value labels\n",
    "for i, v in enumerate(top_products):\n",
    "    plt.text(v + 2, i, str(v), va='center', fontsize=10, fontweight='bold')\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()\n",
    "\n",
    "print(\"\\n💡 Fashion and Electronics dominate our sales!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 🤔 But wait... Which category generates the MOST revenue?\n",
    "\n",
    "Most orders ≠ Most revenue! Let's find out."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate revenue by product category\n",
    "# Hint: Group by 'product_category' and sum 'total_amount'\n",
    "\n",
    "revenue_by_product = # YOUR CODE HERE\n",
    "revenue_by_product = revenue_by_product.sort_values(ascending=False)\n",
    "\n",
    "print(\"Revenue by Product Category (JOD):\")\n",
    "print(\"=\"*50)\n",
    "print(revenue_by_product)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a side-by-side comparison\n",
    "fig, axes = plt.subplots(1, 2, figsize=(16, 6))\n",
    "\n",
    "# Left: Number of orders\n",
    "top_products.sort_values().plot(kind='barh', ax=axes[0], color='lightblue', edgecolor='black')\n",
    "axes[0].set_title('By Order Count', fontsize=14, fontweight='bold')\n",
    "axes[0].set_xlabel('Number of Orders')\n",
    "axes[0].grid(axis='x', alpha=0.3)\n",
    "\n",
    "# Right: Revenue\n",
    "revenue_by_product.sort_values().plot(kind='barh', ax=axes[1], color='lightcoral', edgecolor='black')\n",
    "axes[1].set_title('By Revenue (JOD)', fontsize=14, fontweight='bold')\n",
    "axes[1].set_xlabel('Total Revenue (JOD)')\n",
    "axes[1].grid(axis='x', alpha=0.3)\n",
    "\n",
    "plt.suptitle('Product Category Performance', fontsize=16, fontweight='bold', y=1.02)\n",
    "plt.tight_layout()\n",
    "plt.show()\n",
    "\n",
    "print(\"\\n💡 Electronics has fewer orders but generates high revenue - higher average value!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "## Part 6: Business Question #4\n",
    "### 🎯 Are sales trending up or down over time?\n",
    "\n",
    "Time series analysis helps identify growth patterns and seasonality.\n",
    "\n",
    "**This one is more challenging - let's do it together!**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 1: Convert order_date to datetime format\n",
    "df['order_date'] = pd.to_datetime(df['order_date'])\n",
    "\n",
    "# Verify conversion\n",
    "print(\"✅ Date conversion successful\")\n",
    "print(f\"Date range: {df['order_date'].min()} to {df['order_date'].max()}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 2: Extract month from date\n",
    "df['month'] = df['order_date'].dt.to_period('M')\n",
    "\n",
    "# Step 3: Group by month and sum revenue\n",
    "monthly_sales = df.groupby('month')['total_amount'].sum()\n",
    "\n",
    "print(\"Monthly Sales (JOD):\")\n",
    "print(\"=\"*40)\n",
    "print(monthly_sales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visualize the trend\n",
    "plt.figure(figsize=(12, 6))\n",
    "\n",
    "# Convert period to string for plotting\n",
    "monthly_sales.index = monthly_sales.index.astype(str)\n",
    "monthly_sales.plot(kind='line', marker='o', color='green', linewidth=3, markersize=10)\n",
    "\n",
    "plt.title('Monthly Sales Trend', fontsize=16, fontweight='bold', pad=20)\n",
    "plt.ylabel('Total Revenue (JOD)', fontsize=12)\n",
    "plt.xlabel('Month', fontsize=12)\n",
    "plt.grid(True, alpha=0.3)\n",
    "\n",
    "# Add value labels on points\n",
    "for i, v in enumerate(monthly_sales):\n",
    "    plt.text(i, v + 1000, f'{v:,.0f}', ha='center', fontsize=10, fontweight='bold')\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()\n",
    "\n",
    "# Calculate growth rate\n",
    "aug_sales = monthly_sales.iloc[0]\n",
    "oct_sales = monthly_sales.iloc[2]\n",
    "growth_rate = ((oct_sales - aug_sales) / aug_sales) * 100\n",
    "\n",
    "print(f\"\\n💡 Sales grew by {growth_rate:.1f}% from August to October!\")\n",
    "print(\"This is a positive trend - business is growing! 📈\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "## Part 7: Additional Analysis - Payment Methods\n",
    "\n",
    "Let's explore customer payment preferences."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Count payment methods\n",
    "payment_counts = df['payment_method'].value_counts()\n",
    "\n",
    "print(\"Payment Method Distribution:\")\n",
    "print(\"=\"*50)\n",
    "print(payment_counts)\n",
    "print(\"\\nPercentages:\")\n",
    "print(df['payment_method'].value_counts(normalize=True) * 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a pie chart\n",
    "plt.figure(figsize=(10, 8))\n",
    "colors = ['#ff9999', '#66b3ff', '#99ff99']\n",
    "explode = (0.05, 0.05, 0.05)  # Slightly separate slices\n",
    "\n",
    "payment_counts.plot(kind='pie', \n",
    "                    autopct='%1.1f%%',\n",
    "                    startangle=90,\n",
    "                    colors=colors,\n",
    "                    explode=explode,\n",
    "                    shadow=True,\n",
    "                    textprops={'fontsize': 12, 'fontweight': 'bold'})\n",
    "\n",
    "plt.title('Payment Method Distribution', fontsize=16, fontweight='bold', pad=20)\n",
    "plt.ylabel('')  # Remove default ylabel\n",
    "plt.tight_layout()\n",
    "plt.show()\n",
    "\n",
    "print(\"\\n💡 Credit cards are most popular, but cash on delivery is still significant!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "## Part 8: Your Challenge! 💪\n",
    "\n",
    "Now it's time to apply what you've learned. Complete these exercises on your own:\n",
    "\n",
    "### Challenge 1: City-Product Analysis\n",
    "**Question:** Which product category is most popular in Amman?\n",
    "\n",
    "**Hint:** Filter data for Amman, then count product categories."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# YOUR CODE HERE\n",
    "# Step 1: Filter for Amman only\n",
    "amman_data = \n",
    "\n",
    "# Step 2: Count product categories\n",
    "amman_products = \n",
    "\n",
    "# Display result\n",
    "print(\"Most Popular Products in Amman:\")\n",
    "print(amman_products)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Challenge 2: High-Value Customers\n",
    "**Question:** What percentage of orders are above 200 JOD?\n",
    "\n",
    "**Hint:** Use boolean filtering and calculate the percentage."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# YOUR CODE HERE\n",
    "# Step 1: Count orders above 200 JOD\n",
    "high_value_orders = \n",
    "\n",
    "# Step 2: Calculate percentage\n",
    "percentage = \n",
    "\n",
    "print(f\"Percentage of high-value orders (>200 JOD): {percentage:.1f}%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Challenge 3: Average Order by City\n",
    "**Question:** Which city has the highest average order value?\n",
    "\n",
    "**Hint:** Group by city and calculate mean of total_amount."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# YOUR CODE HERE\n",
    "avg_order_by_city = \n",
    "\n",
    "# Sort and display\n",
    "print(\"Average Order Value by City:\")\n",
    "print(avg_order_by_city.sort_values(ascending=False))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "## Part 9: Summary & Key Insights\n",
    "\n",
    "Let's summarize everything we discovered:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"=\"*80)\n",
    "print(\"KEY BUSINESS INSIGHTS FROM OUR ANALYSIS\")\n",
    "print(\"=\"*80)\n",
    "\n",
    "print(\"\\n1. GEOGRAPHIC PERFORMANCE:\")\n",
    "print(f\"   • Top revenue city: {revenue_by_city.index[0]} ({revenue_by_city.iloc[0]:,.0f} JOD)\")\n",
    "print(f\"   • {revenue_by_city.index[0]} generates {(revenue_by_city.iloc[0]/revenue_by_city.sum()*100):.1f}% of total revenue\")\n",
    "\n",
    "print(\"\\n2. ORDER ECONOMICS:\")\n",
    "print(f\"   • Average order value: {average_order:.2f} JOD\")\n",
    "print(f\"   • Median order value: {median_order:.2f} JOD\")\n",
    "print(f\"   • Total transactions: {len(df)}\")\n",
    "\n",
    "print(\"\\n3. PRODUCT PERFORMANCE:\")\n",
    "print(f\"   • Most ordered category: {top_products.index[0]} ({top_products.iloc[0]} orders)\")\n",
    "print(f\"   • Highest revenue category: {revenue_by_product.index[0]} ({revenue_by_product.iloc[0]:,.0f} JOD)\")\n",
    "\n",
    "print(\"\\n4. SALES TREND:\")\n",
    "print(f\"   • Sales growth (Aug → Oct): {growth_rate:.1f}%\")\n",
    "print(f\"   • Trend: {'📈 GROWING' if growth_rate > 0 else '📉 DECLINING'}\")\n",
    "\n",
    "print(\"\\n5. PAYMENT PREFERENCES:\")\n",
    "print(f\"   • Most popular method: {payment_counts.index[0]} ({payment_counts.iloc[0]} orders)\")\n",
    "\n",
    "print(\"\\n\" + \"=\"*80)\n",
    "print(\"STRATEGIC RECOMMENDATIONS\")\n",
    "print(\"=\"*80)\n",
    "print(\"\\n✅ Focus marketing efforts on Amman (highest revenue)\")\n",
    "print(\"✅ Expand Electronics inventory (high revenue per order)\")\n",
    "print(\"✅ Maintain Fashion stock (highest volume)\")\n",
    "print(\"✅ Optimize for Credit Card payments (most popular)\")\n",
    "print(\"✅ Capitalize on growth momentum (15%+ growth trend)\")\n",
    "print(\"\\n\" + \"=\"*80)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "## 🎉 Congratulations!\n",
    "\n",
    "You've just completed a real data analysis project! You:\n",
    "\n",
    "✅ Loaded and explored a dataset  \n",
    "✅ Performed aggregations and grouping  \n",
    "✅ Calculated statistical measures  \n",
    "✅ Created multiple types of visualizations  \n",
    "✅ Answered business questions with data  \n",
    "✅ Generated actionable insights  \n",
    "\n",
    "### What's Next?\n",
    "\n",
    "1. **Complete the bonus challenges** in `03_bonus_challenges.ipynb`\n",
    "2. **Experiment with the data** - ask your own questions!\n",
    "3. **Check the solutions** in `02_workshop_exercise_SOLUTION.ipynb`\n",
    "4. **Consider the full 70-hour program** to master:\n",
    "   - Advanced SQL queries\n",
    "   - Predictive modeling\n",
    "   - Power BI dashboards\n",
    "   - Machine learning basics\n",
    "   - Real-world capstone projects\n",
    "\n",
    "### Questions?\n",
    "- Email: naasrallahh@gmail.com\n",
    "- GitHub: Check the repo for more resources\n",
    "\n",
    "---\n",
    "\n",
    "**Remember:** Every data analyst started exactly where you are now. The key is practice, curiosity, and persistence.\n",
    "\n",
    "Keep analyzing! 📊🚀"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
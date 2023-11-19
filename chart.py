import matplotlib.pyplot as plt


# Example data
# algorithms = ['Algorithm1', 'Algorithm2', 'Algorithm3']
# execution_times = [10, 15, 8]  # Replace with your actual data
#

# # Create bar chart

# plt.bar(algorithms, execution_times)

# plt.xlabel('Sorting Algorithms')
# plt.ylabel('Execution Time (ms)')
# plt.title('Sorting Algorithm Execution Time Comparison')

# Show the chart
# plt.show()


def showCharts(xlabel, ylabel, title, xarr, yarr):
    plt.bar(xarr, yarr)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

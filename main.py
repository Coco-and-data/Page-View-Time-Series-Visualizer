from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

print("Testing Time Series Visualizer...")
print("=" * 50)

try:
    print("Creating line plot...")
    line_fig = draw_line_plot()
    print("✅ Line plot saved as 'line_plot.png'")
    
    print("Creating bar plot...")
    bar_fig = draw_bar_plot()
    print("✅ Bar plot saved as 'bar_plot.png'")
    
    print("Creating box plots...")
    box_fig = draw_box_plot()
    print("✅ Box plots saved as 'box_plot.png'")
    
    print("\n" + "=" * 50)
    print("🎉 SUCCESS! All visualizations created!")
    print("Check your files for:")
    print("  - line_plot.png")
    print("  - bar_plot.png")
    print("  - box_plot.png")
    
except Exception as e:
    print(f"❌ ERROR: {e}")
    print("Make sure all libraries are installed:")
    print("pip install pandas matplotlib seaborn")

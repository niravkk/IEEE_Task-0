import matplotlib.pyplot as mp
import pandas as pd

data = pd.read_csv("data/processed_student_performance.csv", encoding='utf-8')
names = data["Student"]
final = data["Final_Score"]

#bar graph
mp.bar(names, final)
mp.xticks(rotation=90, fontsize = 4)
mp.title("Names vs Final Marks")
mp.xlabel("Names")
mp.ylabel("Final Marks")
mp.savefig(r"plots\final_scores.png")
mp.show()

#scatter plot
hours = data["Hours_Studied"]
mp.scatter(hours, final)
mp.title("Hours Studied vs Final Marks")
mp.xlabel("Hours Studied")
mp.ylabel("Final Marks")
mp.savefig(r"plots\study_vs_score.png")
mp.show()

#histogram
mp.hist(final)
mp.title("Final Scores")
mp.xlabel("scores")
mp.ylabel("Number of people")
mp.savefig(r"plots\score_distribution.png")
mp.show()

#custom plot
#hours studied vs improvement
hours = data["Hours_Studied"]
imp = data["Improvement"]
mp.scatter(hours, imp)
mp.title("Hours Studied vs Improvement")
mp.xlabel("Hours Studied")
mp.ylabel("Improvement")
mp.savefig(r"plots\custom_plot.png")
mp.show()
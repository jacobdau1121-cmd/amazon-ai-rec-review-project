# The Impact of AI Recommendation Systems on Amazon Product Reviews
**Course:** SUM26001 Final Group Project

## 1. Project Description
### Problem Statement
E-commerce platforms widely adopt AI recommendation systems, yet it remains unclear whether AI-recommended products receive significantly different customer ratings compared to non-recommended items. This project uses Amazon customer review dataset to test whether AI recommendation positively affects user star ratings, and analyzes the correlation between ratings and helpful votes.

### Research Objectives
1. Compare average star ratings & helpful votes between AI-recommended and non-recommended product reviews
2. Use independent sample t-test to verify if rating difference is statistically significant
3. Explore linear correlation between star rating and helpful votes via Pearson correlation analysis
4. Summarize limitations of the analysis and propose future research directions

### Progress & Lessons Learned
We completed full data preprocessing, random sampling of 50,000 reviews, Python statistical analysis with pandas/scipy/matplotlib, and formal academic report writing via Quarto.
Core bottleneck encountered: No official AI recommendation label in original Amazon dataset.
Adjustment: Constructed binary variable `is_ai_recommend` to manually classify two groups for comparative analysis.
Key lesson: Dataset variable completeness directly restricts research precision; future work should seek raw platform recommendation tags for more accurate results.

## 2. Group Members & Individual Contributions
1. Dou Yuhan, Student ID: [202420101149]
   - Select research topic
   - Complete all Python data processing & statistical analysis code
   - Write, structure and revise the full Quarto project report
   - Interpret analysis results, discussion & conclusion writing

2. Yang Haoyuxuan, Student ID: [202420101102]
   - Design presentation PPT slides
   - Compose project presentation script
   - Organize project materials, assist report formatting & proofreading

## 3. Core File Links in Repository

- Final rendered report PDF: [report/project.pdf](report/project.pdf)
- Quarto source file for generating PDF: [report/project.qmd](report/project.qmd)

## 4. Repository File Structure Overview

- analysis.py: Python code for data preprocessing and statistical analysis
- report/project.qmd: Quarto source file
- report/project.pdf: Final rendered report
- .gitignore: Ignore rules for Quarto, Python cache, and datasets
- README.md: Project overview and submission guide
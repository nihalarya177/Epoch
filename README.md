# Epoch's Usable AI - Data-driven insights for everyone, not just for data scientists.

## Try it Out
Stramlit Application:
Video Demo: 

## Inspiration
Our project derives inspiration from the **Stanford DAWN** project, which popularized the term "Usable AI"- an approach to Machine Learning which focuses on delivering interpretable insights to non-technical stakeholders over performance metrics like accuracy.

While there are many Automated Machine Learning libraries available today, such as H2O.ai and PyCaret, these tools typically require a level of prior knowledge and understanding of data analysis. As such, these tools cater to simplify the workflows for Data Scientists rather than to quickly generate actionable insights for the domain users.

Our tool is designed to bridge this gap, democratizing Machine Learning by helping small businesses extract valuable insights from their data without the need for extensive investments in data scientists, engineers, or analysts.

In addition, our tool can serve as an excellent starting point for experts in the field, providing a streamlined and automated solution for tedious tasks. By freeing up their time and energy, they can focus on more complex problems and generate insights with greater efficiency and accuracy.

## What it does
Our tool receives data from the user, performs basic data cleaning and transformations, and applies exploratory analytics, regression, classification, and feature importance methods - all under the hood. The output is presented in the form of easy-to-understand insights without the use of any technical jargon, simple enough that a child can understand them.

At a more involved level, we have created our own variant of the **CARs** (Classification using Association Rules) algorithm for generating classification rules: this algorithm is drastically different from other solutions available, is robust to NANs and can understand complex inferences from the dataset. 

All of this, coupled with a simple and intuitive web interface, makes our tool the ideal solution for businesses looking to unlock the power of Machine Learning without the need for extensive technical knowledge or resources. 

## How we built it
We developed our application using a Python backend and a crafted a Streamlit web app to deliver it to users. To optimize the performance and scalability of our platform, we incorporated several AWS services, such as Lambda functions for serverless, decoupled compute, S3 buckets for scalable storage, and an EC2 instance to deploy our application. With this powerful combination of technologies, we were able to build a robust, reliable, and efficient solution.

## Challenges we ran into
Our biggest challenge was familiarizing ourselves with AWS services over the weekend, but we were able to overcome this by dedicating significant time to studying the AWS documentation, practicing with examples, and taking advantage of online communities and the mentors provided by the competition. As a result, we were able to successfully leverage select AWS services for both building and deploying our project, all the while gaining valuable experience in cloud computing.

## Accomplishments that we're proud of
We are most proud of the innovative Rule Mining Algorithm we implemented, on short notice, that is robust enough to handle a variety of dataset schemas and data types. It not only extracts rules from the data but also conveys them as human readable insights, useful to both domain experts and novices.

We are also excited about our report generator that automates one of the most cumbersome parts of any data science project, the data processing and exploratory data analysis. It performs a comprehensive analysis on the give dataset with special consideration given to categorical variables and messy data.

## What we learned
We gained a comprehensive understanding of the complexities involved in building a rule mining algorithm, as well as the strengths and limitations of existing AutoML solutions in the market. Our team also had the opportunity to gain hands-on experience with AWS and cloud computing, allowing us to expand our skillset and utilize cutting-edge technology to deliver innovative solutions to our clients.

## What's next for Usable AI
Moving forward, we plan to continue improving and refining our Usable AI tool, simplifying the user experience as much as possible without sacrificing on the rigor of our analysis. We also plan to explore additional Machine Learning algorithms and Rule Mining techniques that can be incorporated into our report generation feature to further increase the business value one can extract from our solution.

In addition, we hope to expand our reach and make our tool more accessible to a wider audience, including small businesses and individuals who may not have the resources to invest in data science expertise. We believe that democratizing Machine Learning in this way has the potential to drive significant growth and innovation across a wide range of industries and use cases.

Overall, we are excited to continue pushing the boundaries of what is possible with Usable AI and helping businesses and individuals unlock the full potential of their data.

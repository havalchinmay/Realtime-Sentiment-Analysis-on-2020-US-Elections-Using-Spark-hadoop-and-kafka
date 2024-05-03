# Realtime-Sentiment-Analysis-on-2020-US-Elections-Using-Spark-hadoop-and-kafka
### Team Members:
- Ayush Jain  
- Chinmay Haval 
- Milind Murmu
- Rahul Singh
    
**Dataset:**

https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets

### Prerequisites
- Python 3.x
- Apache Spark
- Kafka
- 
### Setting Up the Environment
1. **Create a Hadoop Spark Cluster**:
   - Follow the instructions to set up a Hadoop Spark cluster.
   - 4 node cluster was made to run this project

2. **Setup Kafka Server**:
   - Install and configure Kafka with a single broker.
   - Create two topics named 'trump' and 'biden'.

3. **Download Dataset**:
   - Download the Twitter dataset and place it in the `data` folder of this repository.

### Running the Project
1. **Run the Spark Consumer**:
   - Open and execute the `spark_streaming.ipynb` notebook to start the Spark streaming application for sentiment analysis.

2. **Start Streaming Tweets**:
   - Run the `tweets_producer.ipynb` notebook to start streaming tweets into Kafka from the dataset.

3. **Visualize the Data**:
   - Execute the `testPlot.py` and `testmap.py` scripts to visualize the sentiment analysis results using Matplotlib and GeoPandas.

### Project Structure
- `data/`: Contains the Twitter dataset.
- `spark_streaming.ipynb`: Spark streaming application for sentiment analysis.
- `tweets_producer.ipynb`: Kafka producer to stream tweets into Kafka.
- `testPlot.py`: Script to visualize sentiment analysis results with a bar graph.
- `testmap.py`: Script to visualize sentiment analysis results on a US state map.

### References
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/index.html)
- [Kafka Documentation](https://kafka.apache.org/documentation/)
  
**Architecture:**

<img src="https://github.com/havalchinmay/Realtime-Sentiment-Analysis-on-2020-US-Elections-Using-Spark-hadoop-and-kafka/assets/125662714/738869f1-c747-4cf7-966d-0ee0fb58a89c" alt="Architecture" width="50%">

**Work flow explanation**

The project aimed to develop a real-time sentiment analysis pipeline for tweets related to the 2020 US presidential election, specifically focusing on the candidates Donald Trump and Joe Biden. The pipeline was built using Apache Spark and leveraged various other technologies, such as Apache Kafka, Spark NLP, and data visualization libraries like Matplotlib and Geopandas.

**Data Ingestion:**

The project used Apache Kafka as a distributed streaming platform to ingest real-time tweet data.
A Kafka producer script was developed to read tweet data from CSV files and publish the tweets to a Kafka topic.

**Spark Streaming Pipeline:**

A Spark Streaming application was built using PySpark to consume the tweet data from the Kafka topic.
The tweet data was then processed through a Spark NLP pipeline, which included components like the DocumentAssembler, UniversalSentenceEncoder, and SentimentDLModel.
The DocumentAssembler preprocessed the raw tweet text, preparing it for the downstream NLP tasks.
The UniversalSentenceEncoder generated sentence embeddings, which are dense vector representations of the tweet text, capturing their semantic meaning.
The SentimentDLModel, a pre-trained deep learning model, performed sentiment analysis on the sentence embeddings, classifying each tweet into positive, negative, or neutral sentiment categories.

**Data Aggregation and Processing:**

The sentiment analysis results were aggregated and processed within the Spark Streaming pipeline.
The processed data, including the tweet text, sentiment scores, and state information, were written to a CSV file in real-time.

**Real-time Visualization:**

The project integrated the Matplotlib and Geopandas libraries for creating interactive and real-time data visualizations.
A choropleth map of the United States was generated using Geopandas, with each state colored based on the overall sentiment of tweets originating from that state.
A custom color mapping function was implemented to assign shades of red for positive sentiment and shades of blue for negative sentiment, with darker shades representing stronger sentiment.
The choropleth map updated dynamically as new sentiment data became available from the Spark Streaming pipeline.

*gif of real time plot*

**Spatial-Temporal Analysis:**

The project enabled spatial-temporal analysis by incorporating state-level information and timestamps into the sentiment data.
This allowed for analyzing sentiment trends across different regions of the United States and over time.
Overall, the project demonstrated the power of Apache Spark, Spark NLP, and real-time data processing and visualization techniques using Matplotlib and Geopandas. It provided a platform for monitoring and analyzing public sentiment towards the 2020 US presidential election candidates in real-time, offering valuable insights into public opinion and potential voting patterns across different states.

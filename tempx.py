def matchingwords(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {words1} with {words2}")
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == "__main__":
    # print(matchingwords("This is good", "Python is is good"))
    sentences = ["Python is good", "this is snake",
                 "Harry is a good boy", "Subscribe to code with harry"]
    
    query=input("Please enter the query string:")
    scores=[matchingwords(query,sentence) for sentence in sentences]
    # print(scores)
    sortedSentSore=[sentScore for sentScore in sorted(zip(scores, sentences), reverse=True)]
    print(f"{len(sortedSentSore)} results found!")
    for score,item in sortedSentSore:
        print(f"\"{item}\": with a score of {score}")
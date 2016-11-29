1. introduce ourselves and topic
2. explain why trees are important - show both data and relationships - have a lot of data - are well structured and do not induce ambiguity into the data;
    explain importance of being able to query them - digitally would be faster than manually by human look up
3. read out prob statement
4. explain db designing methods and good practices. explain how choice of language for parsing matters
5. explain why consistent - because patternless data will be impossible to parse.
    tell the resource used for each category - Treebanks compiled by IIIT-LTRC, Python2.7, python-mysql library/module
6. Db design had to be simplified from original
    parsing non-ascii was done by fixing delimiters
    MySQL does not show native support for non-roman/non-ascii chars. first binary data was stored - wouldn't be queryable. Changes char support to UTF8
7. explain DB fields. give example query.
8. tell what was learnt. reiterate on the importance of treebanks in CL. reiterate importance of storing as digital DB and for computer based querying
9. acknowledge all
10. thank all
11. bibliography for those interested 
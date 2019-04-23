--Query 1  :  Select all Players in Game
SELECT P.PlayerID, P.PlayerName
FROM Betrayal.Game G
	INNER JOIN Betrayal.Player P ON G.GameID = P.GameID
WHERE G.GameID = 2
GROUP BY P.PlayerID, P.PlayerName
ORDER BY PlayerID


--Query 2  :  How many monsters are on the Board in Game
SELECT Count(M.MonsterID) AS MonsterCount
FROM Betrayal.Game G
	INNER JOIN Betrayal.Tile T ON T.GameID = G.GameID
	INNER JOIN Betrayal.Monster M ON M.TileID = M.TileID

--Query 3  :  Select total number of Game sessions
SELECT Count(G.GameID) AS GameCount
FROM Betrayal.Game G


--Query 4  :  Select how many haunt cards have been played in Game
SELECT  Count(C.CardID) AS HauntsPlayed
FROM Betrayal.Game G
	INNER JOIN Betrayal.Card C ON G.GameID = C.GameID
WHERE G.GameID = 2 AND C.Type = 'Haunt' AND C.State = 'Played'

--Query 5  :  Select Items that a specific Player owns
SELECT I.PlayerID, I.Name
FROM Betrayal.Game G
	INNER JOIN Betrayal.Player P ON G.GameID = P.GameID
	INNER JOIN Betrayal.Character C ON P.PlayerID = C.PlayerID
	INNER JOIN Betrayal.Item I ON C.CharacterID = I.CharacterID


--Query 6  :  Select all stats for every character in the Game Session
SELECT CH.CharacterID, CH.CharacterName, CH.Speed, CH.Might, CH.Sanity, CH.Knowledge
FROM Betrayal.Game G
	INNER JOIN Betrayal.Player P ON G.GameID = P.GameID
	INNER JOIN Betrayal.Character CH ON P.PlayerID = CH.PlayerID
WHERE G.GameID = 2
GROUP BY  CH.CharacterID, CH.CharacterName, CH.Speed, CH.Might, CH.Sanity, CH.Knowledge
ORDER BY CH.CharacterID

--Query 7  :  Select all entities on a specific tile
SELECT M.Name, CH.CharacterName, I.Name
FROM Betrayal.Game G
	INNER JOIN Betrayal.Tile T ON G.GameID = T.GameID
	INNER JOIN Betrayal.Character CH ON T.TileID = CH.TileID
	INNER JOIN Betrayal.Monster M ON T.TileID = M.TileID
	INNER JOIN Betrayal.Item I ON T.TileID = I.TileID
WHERE G.GameID = 2 AND T.TileID = 1
GROUP BY M.Name, CH.CharacterName, I.Name


--Query 8  :  Select start date of Game 
SELECT G.GameID, G.StartDate
FROM Betrayal.Game G
WHERE G.GameID = 1
GROUP BY G.GameID, G.StartDate

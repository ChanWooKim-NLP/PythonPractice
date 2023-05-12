-- 코드를 입력하세요
SELECT concat("/home/grep/src/", B.BOARD_ID, "/", FILE_ID, FILE_NAME, FILE_EXT) FILE_PATH
FROM USED_GOODS_BOARD B
    LEFT JOIN USED_GOODS_FILE F ON B.BOARD_ID = F.BOARD_ID
WHERE VIEWS = (SELECT max(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY FILE_ID desc